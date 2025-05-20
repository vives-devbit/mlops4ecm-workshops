#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>
#include <onnxruntime_cxx_api.h>

const char* const EXT_LIB = "../lib/libortextensions.so";
const char* const MODEL_PATH = "../../whisper_end_to_end.onnx";
const char* const AUDIO_PATH = "../../speech.wav";

// Load raw bytes from a file (e.g., a WAV file)
std::vector<uint8_t> load_file_bytes(const std::string& path) {
    std::ifstream file(path, std::ios::binary | std::ios::ate);
    if (!file) throw std::runtime_error("Failed to open file: " + path);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<uint8_t> buffer(size);
    if (!file.read(reinterpret_cast<char*>(buffer.data()), size))
        throw std::runtime_error("Failed to read file: " + path);
    return buffer;
}

int main() {
    Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "run_whisper");
    Ort::SessionOptions session_options;

    // Register ONNX Runtime Extensions
    void* handle = nullptr;
    OrtStatus* status = Ort::GetApi().RegisterCustomOpsLibrary(session_options, EXT_LIB, &handle);
    if (status != nullptr) {
        std::cerr << "Failed to load extensions: " << Ort::GetApi().GetErrorMessage(status) << std::endl;
        return 1;
    }
    std::cout << "ONNX Runtime Extensions registered successfully.\n";

    // Load model
    Ort::Session session(env, MODEL_PATH, session_options);
    std::cout << "Model loaded: " << MODEL_PATH << "\n";

    // Get input/output names
    std::vector<std::string> input_names = session.GetInputNames();
    std::vector<std::string> output_names = session.GetOutputNames();

    std::vector<const char*> input_name_ptrs;
    for (const auto& name : input_names) input_name_ptrs.push_back(name.c_str());
    std::vector<const char*> output_name_ptrs;
    for (const auto& name : output_names) output_name_ptrs.push_back(name.c_str());

    // Load WAV file
    std::vector<uint8_t> audio_data = load_file_bytes(AUDIO_PATH);
    Ort::MemoryInfo memory_info = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);

    std::array<int64_t, 2> audio_shape = {1, static_cast<int64_t>(audio_data.size())};
    Ort::Value audio_tensor = Ort::Value::CreateTensor<uint8_t>(
        memory_info, audio_data.data(), audio_data.size(), audio_shape.data(), audio_shape.size());

    // Scalar inputs
    int32_t max_length = 200;
    int32_t min_length = 0;
    int32_t num_beams = 2;
    int32_t num_return_sequences = 1;
    float length_penalty = 1.0f;
    float repetition_penalty = 1.0f;

    std::array<int64_t, 1> scalar_shape = {1};

    std::vector<Ort::Value> inputs;
    inputs.push_back(std::move(audio_tensor));
    inputs.push_back(Ort::Value::CreateTensor<int32_t>(memory_info, &max_length, 1, scalar_shape.data(), scalar_shape.size()));
    inputs.push_back(Ort::Value::CreateTensor<int32_t>(memory_info, &min_length, 1, scalar_shape.data(), scalar_shape.size()));
    inputs.push_back(Ort::Value::CreateTensor<int32_t>(memory_info, &num_beams, 1, scalar_shape.data(), scalar_shape.size()));
    inputs.push_back(Ort::Value::CreateTensor<int32_t>(memory_info, &num_return_sequences, 1, scalar_shape.data(), scalar_shape.size()));
    inputs.push_back(Ort::Value::CreateTensor<float>(memory_info, &length_penalty, 1, scalar_shape.data(), scalar_shape.size()));
    inputs.push_back(Ort::Value::CreateTensor<float>(memory_info, &repetition_penalty, 1, scalar_shape.data(), scalar_shape.size()));

    std::cout << "Running inference...\n";
    auto output_tensors = session.Run(
        Ort::RunOptions{nullptr},
        input_name_ptrs.data(),
        inputs.data(),
        inputs.size(),
        output_name_ptrs.data(),
        output_name_ptrs.size()
    );

    // Extract string output
    size_t str_len = output_tensors[0].GetStringTensorElementLength(0);
    std::string result(str_len, '\0');
    output_tensors[0].GetStringTensorElement(str_len, 0, result.data());

    std::cout << "\nTranscription:\n" << result << "\n";
    return 0;
}

