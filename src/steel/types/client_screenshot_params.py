# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientScreenshotParams"]


class ClientScreenshotParams(TypedDict, total=False):
    url: Required[str]
    """URL of the webpage to capture"""

    use_proxy: Annotated[bool, PropertyInfo(alias="useProxy")]
    """Use a Steel-provided residential proxy for capturing the screenshot"""