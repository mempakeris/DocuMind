import boto3
from mypy_boto3_s3.client import S3Client
from src.settings import settings

_storage_client: S3Client = boto3.client(
    "s3",
    endpoint_url=settings.minio_endpoint,
    aws_access_key_id=settings.minio_root_user,
    aws_secret_access_key=settings.minio_root_password,
    region_name="us-east-1",
)


def get_storage_client():
    return _storage_client
