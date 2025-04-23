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
    name: Required[str]
    """The name of the cookie"""

    value: Required[str]
    """The value of the cookie"""

    domain: str
    """The domain of the cookie"""

    expires: float
    """The expiration date of the cookie"""

    http_only: Annotated[bool, PropertyInfo(alias="httpOnly")]
    """Whether the cookie is HTTP only"""

    partition_key: Annotated[str, PropertyInfo(alias="partitionKey")]
    """The partition key of the cookie"""

    path: str
    """The path of the cookie"""

    priority: Literal["Low", "Medium", "High"]
    """The priority of the cookie"""

    same_party: Annotated[bool, PropertyInfo(alias="sameParty")]
    """Whether the cookie is a same party cookie"""

    same_site: Annotated[Literal["Strict", "Lax", "None"], PropertyInfo(alias="sameSite")]
    """The same site attribute of the cookie"""

    secure: bool
    """Whether the cookie is secure"""

    session: bool
    """Whether the cookie is a session cookie"""

    size: float
    """The size of the cookie"""

    source_port: Annotated[float, PropertyInfo(alias="sourcePort")]
    """The source port of the cookie"""

    source_scheme: Annotated[Literal["Unset", "NonSecure", "Secure"], PropertyInfo(alias="sourceScheme")]
    """The source scheme of the cookie"""

    url: str
    """The URL of the cookie"""


class SessionContext(TypedDict, total=False):
    cookies: Iterable[SessionContextCookie]
    """Cookies to initialize in the session"""

    indexed_db: Annotated[Dict[str, Iterable[Dict[str, object]]], PropertyInfo(alias="indexedDB")]
    """Domain-specific indexedDB items to initialize in the session"""

    local_storage: Annotated[Dict[str, Dict[str, object]], PropertyInfo(alias="localStorage")]
    """Domain-specific localStorage items to initialize in the session"""

    session_storage: Annotated[Dict[str, Dict[str, object]], PropertyInfo(alias="sessionStorage")]
    """Domain-specific sessionStorage items to initialize in the session"""
