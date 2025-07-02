# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Sessionslist", "Session", "SessionDimensions", "SessionStealthConfig"]


class SessionDimensions(BaseModel):
    height: int
    """Height of the browser window"""

    width: int
    """Width of the browser window"""


class SessionStealthConfig(BaseModel):
    humanize_interactions: Optional[bool] = FieldInfo(alias="humanizeInteractions", default=None)
    """
    This flag will make the browser act more human-like by moving the mouse in a
    more natural way
    """

    skip_fingerprint_injection: Optional[bool] = FieldInfo(alias="skipFingerprintInjection", default=None)
    """This flag will skip the fingerprint generation for the session."""


class Session(BaseModel):
    id: str
    """Unique identifier for the session"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the session started"""

    credits_used: int = FieldInfo(alias="creditsUsed")
    """Amount of credits consumed by the session"""

    debug_url: str = FieldInfo(alias="debugUrl")
    """URL for debugging the session"""

    dimensions: SessionDimensions
    """Viewport and browser window dimensions for the session"""

    duration: int
    """Duration of the session in milliseconds"""

    event_count: int = FieldInfo(alias="eventCount")
    """Number of events processed in the session"""

    proxy_bytes_used: int = FieldInfo(alias="proxyBytesUsed")
    """Amount of data transmitted through the proxy"""

    proxy_source: Optional[Literal["steel", "external"]] = FieldInfo(alias="proxySource", default=None)
    """Source of the proxy used for the session"""

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

    region: Optional[Literal["lax", "ord", "iad", "bom", "scl", "fra", "hkg"]] = None
    """The region where the session was created"""

    solve_captcha: Optional[bool] = FieldInfo(alias="solveCaptcha", default=None)
    """Indicates if captcha solving is enabled"""

    stealth_config: Optional[SessionStealthConfig] = FieldInfo(alias="stealthConfig", default=None)
    """Stealth configuration for the session"""

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)
    """User agent string used in the session"""


class Sessionslist(BaseModel):
    sessions: List[Session]
    """List of browser sessions"""
