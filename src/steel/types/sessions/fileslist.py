# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Fileslist", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier for the file"""

    checksum: str
    """Checksum or hash of the file content for integrity verification"""

    content_type: str = FieldInfo(alias="contentType")
    """MIME type of the file"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the file was created"""

    name: str
    """Name of the file"""

    path: str
    """Path to the file in the storage system"""

    size: float
    """Size of the file in bytes"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the file was last updated"""

    metadata: Optional[Dict[str, object]] = None
    """Custom metadata associated with the file"""


class Fileslist(BaseModel):
    data: List[Data]
    """Array of files for the current page"""
