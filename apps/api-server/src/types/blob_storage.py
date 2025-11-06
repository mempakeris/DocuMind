from pydantic import BaseModel, UUID4, Field


class UploadURLResponse(BaseModel):
    upload_url: str
    expires_in: int


class UploadURLRequest(BaseModel):
    user_id: UUID4 = Field(description="The User ID represented as UUID4")
    filename: str = Field(max_length=256, description="Name of the file to upload")
