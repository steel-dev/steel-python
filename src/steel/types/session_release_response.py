# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SessionReleaseResponse"]


class SessionReleaseResponse(BaseModel):
    """Response for releasing a single session."""

    message: str
    """Details about the outcome of the release operation"""

    success: bool
    """Indicates if the session was successfully released"""
