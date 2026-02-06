# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import FileTypes

__all__ = ["ExtensionUploadParams"]


class ExtensionUploadParams(TypedDict, total=False):
    file: FileTypes
    """Extension .zip/.crx file"""

    url: str
    """Extension URL"""
