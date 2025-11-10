from fastapi import APIRouter, Body
from src.types import blob_storage as blob_storage_types
from src.services import blob_storage as blob_storage_services

router = APIRouter(prefix="/storage", tags=["storage"])


@router.post("/upload-url")
def create_upload_url(
    request: blob_storage_types.UploadURLRequest,
) -> blob_storage_types.UploadURLResponse:
    # TODO: Support files over 5GB
    return blob_storage_services.get_upload_url(
        user_id=request.user_id, filename=request.filename
    )
