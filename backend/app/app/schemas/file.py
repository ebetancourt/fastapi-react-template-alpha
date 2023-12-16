from typing import Optional

from pydantic import BaseModel


# Shared properties
class FileBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    summary: Optional[str] = None
    s3_location: Optional[str] = None
    owner_id: Optional[int] = None
    indexed: bool = False


# Properties to receive on File creation
class FileCreate(FileBase):
    name: str
    description: Optional[str] = None
    summary: Optional[str] = None
    s3_location: Optional[str] = None
    owner_id: Optional[int] = None
    indexed: bool = False


# Properties to receive on File update
class FileUpdate(FileBase):
    pass


# Properties shared by models stored in DB
class FileInDBBase(FileBase):
    id: int
    name: str
    description: Optional[str] = None
    summary: Optional[str] = None
    s3_location: Optional[str] = None
    owner_id: int
    indexed: bool = False

    class Config:
        orm_mode = True


# Properties to return to client
class File(FileInDBBase):
    pass


# Properties properties stored in DB
class FileInDB(FileInDBBase):
    pass
