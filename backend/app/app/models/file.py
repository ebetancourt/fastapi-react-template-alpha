from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class File(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    summary = Column(String)
    s3_location = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="files")
    indexed = Column(Boolean, default=False)
