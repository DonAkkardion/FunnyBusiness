from urllib.parse import urlparse, urlunparse
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class CustomS3Boto3Storage(S3Boto3Storage):

    def url(self, name):
        original_url = super().url(name)
        if settings.MINIO_PUBLIC_URL:
            url_parts = urlparse(original_url)
            public_url_parts = urlparse(settings.MINIO_PUBLIC_URL)
            original_url = urlunparse(
                (
                    public_url_parts.scheme,
                    public_url_parts.netloc,
                    url_parts.path,
                    url_parts.params,
                    url_parts.query,
                    url_parts.fragment,
                )
            )
        return original_url