# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Session", "Dimensions", "OptimizeBandwidth", "DeviceConfig", "StealthConfig"]


class Dimensions(BaseModel):
    height: int
    """Height of the browser window"""

    width: int
    """Width of the browser window"""


class OptimizeBandwidth(BaseModel):
    block_hosts: Optional[List[str]] = FieldInfo(alias="blockHosts", default=None)

    block_images: Optional[bool] = FieldInfo(alias="blockImages", default=None)

    block_media: Optional[bool] = FieldInfo(alias="blockMedia", default=None)

    block_stylesheets: Optional[bool] = FieldInfo(alias="blockStylesheets", default=None)

    block_url_patterns: Optional[List[str]] = FieldInfo(alias="blockUrlPatterns", default=None)


class DeviceConfig(BaseModel):
    device: Optional[Literal["desktop", "mobile"]] = None


class StealthConfig(BaseModel):
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

    dimensions: Dimensions
    """Viewport and browser window dimensions for the session"""

    duration: int
    """Duration of the session in milliseconds"""

    event_count: int = FieldInfo(alias="eventCount")
    """Number of events processed in the session"""

    headless: bool
    """Indicates if the session is headless or headful"""

    optimize_bandwidth: OptimizeBandwidth = FieldInfo(alias="optimizeBandwidth")
    """Bandwidth optimizations that were applied to the session."""

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

    device_config: Optional[DeviceConfig] = FieldInfo(alias="deviceConfig", default=None)
    """Device configuration for the session"""

    is_selenium: Optional[bool] = FieldInfo(alias="isSelenium", default=None)
    """Indicates if Selenium is used in the session"""

    persist_profile: Optional[bool] = FieldInfo(alias="persistProfile", default=None)
    """This flag will persist the profile for the session."""

    profile_id: Optional[str] = FieldInfo(alias="profileId", default=None)
    """The ID of the profile associated with the session"""

    region: Optional[Literal["lax", "ord", "iad", "scl", "fra"]] = None
    """The region where the session was created"""

    solve_captcha: Optional[bool] = FieldInfo(alias="solveCaptcha", default=None)
    """Indicates if captcha solving is enabled"""

    stealth_config: Optional[StealthConfig] = FieldInfo(alias="stealthConfig", default=None)
    """Stealth configuration for the session"""

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)
    """User agent string used in the session"""
