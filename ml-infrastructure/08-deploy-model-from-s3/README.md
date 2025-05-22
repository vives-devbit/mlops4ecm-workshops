
# 08 – Deploy Model from S3

<img src="../../media/s3-minio-logos-name.jpg" style="width: 300px" align="right">

> Set up a local S3-compatible storage server (MinIO), upload your trained model, and configure your API to load the model from S3.

Set up a local MinIO S3-compatible server. Upload your trained model to an S3 bucket and modify your API to load the model directly from S3 instead of disk. This simulates real-world production model storage.

So your fastapi has to download the model from S3 during startup.
It could even monitor S3 for new uploads, so models are auto deployed!

