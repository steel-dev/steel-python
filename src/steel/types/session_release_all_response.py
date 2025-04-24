# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SessionReleaseAllResponse"]


class SessionReleaseAllResponse(BaseModel):
    message: str
    """Details about the outcome of the release operation"""

    success: bool
    """Indicates if the sessions were successfully released"""
