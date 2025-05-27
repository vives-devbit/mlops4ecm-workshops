import boto3
import os

# Load environment variables
MINIO_ROOT_USER = os.getenv("MINIO_ROOT_USER")
MINIO_ROOT_PASSWORD = os.getenv("MINIO_ROOT_PASSWORD")
MINIO_ENDPOINT_URL = os.getenv("MINIO_ENDPOINT_URL")
MINIO_BUCKET = os.getenv("MINIO_BUCKET")

# Check environment variables are set
assert MINIO_ROOT_USER is not None
assert MINIO_ROOT_PASSWORD is not None
assert MINIO_ENDPOINT_URL is not None
assert MINIO_BUCKET is not None

def create_s3_client():
    """Create and return a boto3 S3 client using environment variables."""
    return boto3.client(
        "s3",
        endpoint_url=MINIO_ENDPOINT_URL,
        aws_access_key_id=MINIO_ROOT_USER,
        aws_secret_access_key=MINIO_ROOT_PASSWORD,
    )

def upload_to_s3(file_path):
    """Upload a file to S3-compatible storage using boto3."""
    bucket = MINIO_BUCKET
    object_name = file_path
    s3 = create_s3_client()

    # ❗ TODO: Upload the file to the S3 bucket
    raise NotImplementedError("upload_to_s3() is not implemented yet.")

    print(f"✅ Uploaded {file_path} => s3://{bucket}/{object_name}")

def download_from_s3(file_path):
    """Download a file from S3-compatible storage using boto3."""
    bucket = MINIO_BUCKET
    object_name = file_path
    s3 = create_s3_client()
    s3.download_file(bucket, object_name, file_path)
    print(f"✅ Downloaded s3://{bucket}/{object_name} => {file_path}")
