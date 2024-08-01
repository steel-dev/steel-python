# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["DeleteSessionResponse"]


class DeleteSessionResponse(BaseModel):
    success: bool
    """Indicates whether the session was successfully deleted"""
