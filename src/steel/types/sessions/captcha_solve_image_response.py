# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CaptchaSolveImageResponse"]


class CaptchaSolveImageResponse(BaseModel):
    success: bool
    """Whether the action was successful"""

    message: Optional[str] = None
    """Response message"""
