# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientScreenshotParams"]


class ClientScreenshotParams(TypedDict, total=False):
    url: Required[str]
    """URL of the webpage to capture"""

    delay: float
    """Delay before capturing the screenshot (in milliseconds)"""

    full_page: Annotated[bool, PropertyInfo(alias="fullPage")]
    """Capture the full page screenshot. Default is `false`."""

    region: str
    """The desired region for the action to be performed in"""

    use_proxy: Annotated[bool, PropertyInfo(alias="useProxy")]
    """Use a Steel-provided residential proxy for capturing the screenshot"""
