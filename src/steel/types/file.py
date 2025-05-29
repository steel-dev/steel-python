# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    last_modified: datetime = FieldInfo(alias="lastModified")
    """Timestamp when the file was created"""

    path: str
    """Path to the file in the storage system"""

    size: float
    """Size of the file in bytes"""
