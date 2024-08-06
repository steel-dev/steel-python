# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    duration: int
    """Duration of the session in seconds (updates in real-time for live sessions)"""

    event_count: int = FieldInfo(alias="eventCount")
    """
    Number of events that occurred in the session (updates in real-time for live
    sessions)
    """

    is_live: bool = FieldInfo(alias="isLive")
    """Indicates if the session is currently active"""

    session_id: str = FieldInfo(alias="sessionId")
    """Unique identifier for the session"""

    session_timeout: int = FieldInfo(alias="sessionTimeout")
    """When to timeout session in milliseconds"""

    start_date: datetime = FieldInfo(alias="startDate")
    """Timestamp when the session was started"""

    stealth_mode: bool = FieldInfo(alias="stealthMode")
    """Indicates if stealth mode is enabled for the session"""

    websocket_url: str = FieldInfo(alias="websocketUrl")
    """WebSocket URL for connecting to the session"""

    debug_url: Optional[str] = FieldInfo(alias="debugUrl", default=None)
    """debug URL for debugging or embedding the session"""

    session_viewer_url: Optional[str] = FieldInfo(alias="sessionViewerUrl", default=None)
    """URL for viewing the session in the Steel Session Viewer"""
