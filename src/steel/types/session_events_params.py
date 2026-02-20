# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionEventsParams"]


class SessionEventsParams(TypedDict, total=False):
    compressed: bool
    """Compress the events"""

    limit: int
    """Optional pagination limit"""

    pointer: str
    """Pagination pointer"""
