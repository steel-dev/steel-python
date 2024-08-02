# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionListResponse", "Session"]


class Session(BaseModel):
    duration: int
    """Duration of the session in seconds"""

    event_count: int = FieldInfo(alias="eventCount")
    """Number of events that occurred in the session"""

    is_live: bool = FieldInfo(alias="isLive")
    """Indicates if the session is currently active"""

    session_id: str = FieldInfo(alias="sessionId")
    """Unique identifier for the session"""

    start_date: datetime = FieldInfo(alias="startDate")
    """Timestamp when the session was started"""

    timeout: int
    """When to timeout session in ms."""

    websocket_url: str = FieldInfo(alias="websocketUrl")
    """WebSocket URL for connecting to the session"""


class SessionListResponse(BaseModel):
    sessions: List[Session]
