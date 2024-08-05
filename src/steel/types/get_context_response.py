# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GetContextResponse", "Details"]


class Details(BaseModel):
    proxy: Optional[str] = None
    """Proxy settings for the context"""


class GetContextResponse(BaseModel):
    id: str
    """Unique identifier for the context"""

    details: Details
