from typing import Any, List
from uuid import uuid4
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.services.file_store import generate_file_upload_url, S3PostData
from app.services.job_queue import create_index_file_job

router = APIRouter()


class CreateFileResponse(BaseModel):
    id: str
    name: str
    post_data: S3PostData
    location: str


@router.get("/", response_model=List[schemas.File])
def read_files(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve files.
    """
    if crud.user.is_superuser(current_user):
        files = crud.file.get_multi(db, skip=skip, limit=limit)
    else:
        files = crud.file.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return files


@router.post("/", response_model=schemas.File)
async def create_file(
    *,
    db: Session = Depends(deps.get_db),
    file_in: schemas.FileCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> CreateFileResponse:
    """
    Create new file.
    """
    file_data = file_in
    file_id = str(uuid4())
    s3_data = generate_file_upload_url(file_id, input.name)
    file_data.location = s3_data["location"]
    await crud.file.create_with_owner(
        db=db, obj_in=file_data, owner_id=current_user.id
    )  # Create job in processing queue
    create_index_file_job(file_id, s3_data["location"])
    return CreateFileResponse(
        id=file_id,
        name=input.name,
        post_data=file_data["post_data"],
        location=file_data["location"],
    )
