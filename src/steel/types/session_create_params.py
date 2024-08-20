# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    proxy: str
    """Proxy configuration for the browser session"""

    region: Literal["CA", "US", "FR"]
    """Region for the browser session"""

    session_context: Annotated[object, PropertyInfo(alias="sessionContext")]
    """Custom session context data to be used in the created sessio"""

    session_timeout: Annotated[int, PropertyInfo(alias="sessionTimeout")]
    """How long after starting should the session timeout (in milliseconds)."""

    solve_captcha: Annotated[bool, PropertyInfo(alias="solveCaptcha")]
    """Flag to enable automatic captcha solving"""

    stealth_mode: Annotated[bool, PropertyInfo(alias="stealthMode")]
    """Flag to enable stealth mode for the browser session (default: false)"""

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]
    """Custom user agent string for the browser session"""
