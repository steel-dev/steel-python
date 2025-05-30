# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    file: object
    """The file to upload (binary) or URL string to download from"""

    path: str
    """Path to the file in the storage system"""
