# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PdfResponse"]


class PdfResponse(BaseModel):
    url: str
    """URL where the PDF is hosted"""
