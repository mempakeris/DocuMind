from src.clients import blob_storage as blob_storage_client
from src.constants import blob_storage as blob_storage_constants
from src.settings import settings
import uuid

from src.types.blob_storage import UploadURLResponse


def get_upload_url(user_id: str, filename: str) -> UploadURLResponse:
    client = blob_storage_client.get_storage_client()
    upload_url = client.generate_presigned_url(
        "put_object",
        Params={
            "Bucket": settings.document_bucket,
            "Key": f"users/{user_id}/{uuid.uuid4()}_{filename}",
        },
        ExpiresIn=blob_storage_constants.EXPIRES_IN,
    )
    return UploadURLResponse(
        upload_url=upload_url, expires_in=blob_storage_constants.EXPIRES_IN
    )
