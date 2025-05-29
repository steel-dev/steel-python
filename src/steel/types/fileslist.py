# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Fileslist", "Data"]


class Data(BaseModel):
    last_modified: datetime = FieldInfo(alias="lastModified")
    """Timestamp when the file was created"""

    path: str
    """Path to the file in the storage system"""

    size: float
    """Size of the file in bytes"""


class Fileslist(BaseModel):
    data: List[Data]
    """Array of files for the current page"""
