# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CaptchaSolveParams"]


class CaptchaSolveParams(TypedDict, total=False):
    page_id: Annotated[str, PropertyInfo(alias="pageId")]
    """The page ID where the captcha is located"""

    task_id: Annotated[str, PropertyInfo(alias="taskId")]
    """The task ID of the specific captcha to solve"""

    url: str
    """The URL where the captcha is located"""
