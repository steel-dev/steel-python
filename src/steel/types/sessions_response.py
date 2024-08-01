# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionsResponse", "Session"]


class Session(BaseModel):
    id: str
    """Unique identifier for the session"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the session was created"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the session was last updated"""

    websocket_url: Optional[str] = FieldInfo(alias="websocketUrl", default=None)
    """WebSocket URL for connecting to the session"""


class SessionsResponse(BaseModel):
    sessions: List[Session]
