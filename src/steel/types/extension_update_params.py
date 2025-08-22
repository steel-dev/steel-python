# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtensionUpdateParams"]


class ExtensionUpdateParams(TypedDict, total=False):
    file: object
    """Extension .zip/.crx file"""

    url: str
    """Extension URL"""
