# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TopLevelListParams"]


class TopLevelListParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination, use the `next_cursor` from the previous response"""

    limit: int
    """Number of sessions to return per request (default: 25, max: 100)"""

    live_only: bool
    """Flag to retrieve only live sessions (default: true)"""
