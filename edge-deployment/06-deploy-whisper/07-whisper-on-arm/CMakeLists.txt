cmake_minimum_required(VERSION 3.10)
project(onnx_runtime_extensions_test)

set(CMAKE_CXX_STANDARD 17)

# Define relative paths
set(ONNXRUNTIME_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/include")
set(ONNXRUNTIME_LIBRARY_DIR "${CMAKE_SOURCE_DIR}/lib")

# Include and link
include_directories("${ONNXRUNTIME_INCLUDE_DIR}")
link_directories("${ONNXRUNTIME_LIBRARY_DIR}")

# Executable
add_executable(main main.cpp)

# Link ONNX Runtime
target_link_libraries(main onnxruntime)

