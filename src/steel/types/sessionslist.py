# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Sessionslist", "Session"]


class Session(BaseModel):
    id: str
    """Unique identifier for the session"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the session started"""

    credits_used: int = FieldInfo(alias="creditsUsed")
    """Amount of credits consumed by the session"""

    debug_url: str = FieldInfo(alias="debugUrl")
    """URL for debugging the session"""

    duration: int
    """Duration of the session in milliseconds"""

    event_count: int = FieldInfo(alias="eventCount")
    """Number of events processed in the session"""

    session_viewer_url: str = FieldInfo(alias="sessionViewerUrl")
    """URL to view session details"""

    status: Literal["live", "released", "failed"]
    """Status of the session"""

    timeout: int
    """Session timeout duration in milliseconds"""

    websocket_url: str = FieldInfo(alias="websocketUrl")
    """URL for the session's WebSocket connection"""

    is_selenium: Optional[bool] = FieldInfo(alias="isSelenium", default=None)
    """Indicates if Selenium is used in the session"""

    proxy: Optional[str] = None
    """Proxy server used for the session"""

    solve_captcha: Optional[bool] = FieldInfo(alias="solveCaptcha", default=None)
    """Indicates if captcha solving is enabled"""

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)
    """User agent string used in the session"""


class Sessionslist(BaseModel):
    sessions: List[Session]
    """List of browser sessions"""
