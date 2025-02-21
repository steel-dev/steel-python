# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionCreateParams", "Dimensions", "SessionContext", "SessionContextCookie"]


class SessionCreateParams(TypedDict, total=False):
    block_ads: Annotated[bool, PropertyInfo(alias="blockAds")]
    """Block ads in the browser session. Default is false."""

    concurrency: int
    """Number of sessions to create concurrently (check your plan limit)"""

    dimensions: Dimensions
    """Viewport and browser window dimensions for the session"""

    is_selenium: Annotated[bool, PropertyInfo(alias="isSelenium")]
    """Enable Selenium mode for the browser session (default is false).

    Use this when you plan to connect to the browser session via Selenium.
    """

    proxy_url: Annotated[str, PropertyInfo(alias="proxyUrl")]
    """Custom proxy URL for the browser session.

    Overrides useProxy, disabling Steel-provided proxies in favor of your specified
    proxy. Format: http(s)://username:password@hostname:port
    """

    session_context: Annotated[SessionContext, PropertyInfo(alias="sessionContext")]
    """Session context data to be used in the created session.

    Sessions will start with an empty context by default.
    """

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Optional custom UUID for the session"""

    solve_captcha: Annotated[bool, PropertyInfo(alias="solveCaptcha")]
    """Enable automatic captcha solving. Default is false."""

    api_timeout: Annotated[int, PropertyInfo(alias="timeout")]
    """Session timeout duration in milliseconds. Default is 300000 (5 minutes)."""

    use_proxy: Annotated[bool, PropertyInfo(alias="useProxy")]
    """Enable Steel-provided residential proxy usage for the browser session.

    Default is false, which routes requests through datacenter proxies.
    """

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]
    """Custom user agent string for the browser session"""


class Dimensions(TypedDict, total=False):
    height: Required[int]
    """Height of the session"""

    width: Required[int]
    """Width of the session"""


class SessionContextCookie(TypedDict, total=False):
    domain: Required[str]
    """Domain the cookie belongs to"""

    name: Required[str]
    """Name of the cookie"""

    value: Required[str]
    """Value of the cookie"""

    expires: float
    """Unix timestamp when the cookie expires"""

    http_only: Annotated[bool, PropertyInfo(alias="httpOnly")]
    """Whether the cookie is HTTP only"""

    path: str
    """Path the cookie is valid for"""

    same_site: Annotated[Literal["Strict", "Lax", "None"], PropertyInfo(alias="sameSite")]
    """SameSite attribute of the cookie"""

    secure: bool
    """Whether the cookie requires HTTPS"""


class SessionContext(TypedDict, total=False):
    cookies: Iterable[SessionContextCookie]
    """Cookies to initialize in the session"""

    local_storage: Annotated[Dict[str, Dict[str, object]], PropertyInfo(alias="localStorage")]
    """Domain-specific localStorage items to initialize in the session"""
