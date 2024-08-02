# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["ReleaseSessionResponse"]


class ReleaseSessionResponse(BaseModel):
    message: str
    """A message describing the result of the release operation"""

    success: bool
    """Indicates whether the session was successfully released"""
