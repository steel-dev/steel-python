# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["ContextCreateResponse"]


class ContextCreateResponse(BaseModel):
    id: str
    """Unique identifier for the created context"""
