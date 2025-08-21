# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtensionUploadResponse"]


class ExtensionUploadResponse(BaseModel):
    created_at: str = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    extension_id: str = FieldInfo(alias="extensionId")
    """Unique extension identifier (e.g., ext_12345)"""

    name: str
    """Extension name"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""
