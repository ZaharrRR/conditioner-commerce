import boto3
from botocore.exceptions import ClientError

from core import settings, logger

ALLOWED_IMAGE_TYPES = {"image/png", "image/jpeg", "image/jpg"}
MAX_IMAGE_SIZE = 3 * 1024 * 1024  # 3 МБ

class S3Service:
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=settings.s3.access_key,
            aws_secret_access_key=settings.s3.secret_key,
            region_name=settings.s3.region,
        )
        self.s3 = self.session.client("s3", endpoint_url=settings.s3.endpoint)
        self.bucket_name = settings.s3.bucket_name

    def upload_file(self, file_content: bytes, key: str) -> str:
        try:
            self.s3.put_object(Bucket=self.bucket_name, Key=key, Body=file_content)
            return f"{settings.s3.endpoint}/{key}"
        except ClientError as e:
            logger.error(e)
            raise Exception(e)