# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    file: object
    """The file to upload (binary)"""

    file_url: Annotated[str, PropertyInfo(alias="fileUrl")]
    """Public URL to download file from"""

    metadata: Dict[str, object]
    """Custom metadata to associate with the file"""

    name: str
    """Filename to use in session"""
