
# Lab 06 – Optimize Deployment with ONNX Runtime

TODO now that we understand the whisper model, let's deploy it to an edge device using onnx runtime. Model inference with hugging face brings in many large dependencies: python, pytorch, etc... It's not the most efficient on CPU, RAM, etc... We will export our model to ONNX format first and then deploy it with only ONNX Runtime as a dependency. First through python and later only with C++. This is efficient and light-weight.

TODO first export the model using 04-export-whisper-onnx.py, this create a "monolithic" ONNX model with everything in it: pre-precessing audio into mel spectrogram, audio encoding, text decoding, post-processing tokens to text

TODO run this monolith from python with only ONNX runtime as a dependancy: 05-run-whisper-onnx.py
This simply demonstrates that our ONNX model works. A good sanity check before moving to C++.

TODO now compile the cmake project in 06-whisper-from-cpp/ on the server, and run whisper on the server through C++

TODO then do the same thing on our arm board. You will have to clone the repo there first.
We are not doing cross compilation here, just because our linux board is very powerful.
But of course you could do that as well.

Next up: export the whisper model with int8 precision and deploy it again on the linux board.

TODO can you benchmark how long it takes for the model to transcribe your audio? Is the int8 model faster? The simplest/dummest benchmark is just using the `time` command on linux, better is to write a benchmark loop in your c++ code and time it there.

That's it! Nice job
