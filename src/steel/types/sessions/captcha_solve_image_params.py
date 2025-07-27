# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CaptchaSolveImageParams"]


class CaptchaSolveImageParams(TypedDict, total=False):
    image_x_path: Required[Annotated[str, PropertyInfo(alias="imageXPath")]]
    """XPath to the captcha image element"""

    input_x_path: Required[Annotated[str, PropertyInfo(alias="inputXPath")]]
    """XPath to the captcha input element"""

    url: str
    """URL where the captcha is located. Defaults to the current page URL"""
