# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["SteelContextDeleteContextResponse"]


class SteelContextDeleteContextResponse(BaseModel):
    message: str
    """A message indicating the result of the delete operation"""
