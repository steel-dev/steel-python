# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    cursor_id: Annotated[str, PropertyInfo(alias="cursorId")]
    """Cursor ID for pagination"""

    limit: int
    """Number of sessions to return. Default is 50."""

    status: Literal["live", "released", "failed"]
    """Filter sessions by current status"""
