# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TopLevelScreenshotParams"]


class TopLevelScreenshotParams(TypedDict, total=False):
    url: Required[str]
    """The URL of the webpage to screenshot"""
