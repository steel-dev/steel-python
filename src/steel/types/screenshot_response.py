# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ScreenshotResponse"]


class ScreenshotResponse(BaseModel):
    url: str
    """URL where the screenshot is hosted"""
