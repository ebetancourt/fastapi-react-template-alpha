from pydantic import BaseModel
from app.core.config import s3_settings
import os
from boto3 import session

s3_session = session.Session()
file_store_client = s3_session.client(
    "s3",
    region_name=s3_settings["REGION"],
    endpoint_url=s3_settings["ENDPOINT_URL"],
    aws_access_key_id=s3_settings["ACCESS_KEY"],
    aws_secret_access_key=s3_settings["SECRET_KEY"],
)


class S3PostData(BaseModel):
    url: str
    fields: dict


class GenerateFileUploadUrlResponse(BaseModel):
    post_data: S3PostData
    location: str


def generate_file_upload_url(
    file_id,
    file_name,
) -> GenerateFileUploadUrlResponse:
    """
    Generate a pre-signed URL for uploading a file to S3.
    """
    _, extension = os.path.splitext(file_name)
    response = file_store_client.generate_presigned_post(
        s3_settings["BUCKET_NAME"],
        f"{file_id}{extension}",
        ExpiresIn=3600,
    )
    bucket_url = s3_settings["ENDPOINT_URL"]
    location = f"{bucket_url}/{file_id}{extension}"

    return {
        "post_data": S3PostData(**response),
        "location": location,
    }
