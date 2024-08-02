# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SteelContextCreateContextParams"]


class SteelContextCreateContextParams(TypedDict, total=False):
    proxy: str
    """Proxy settings for the context"""
