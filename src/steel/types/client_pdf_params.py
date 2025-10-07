# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientPdfParams"]


class ClientPdfParams(TypedDict, total=False):
    url: Required[str]
    """URL of the webpage to convert to PDF"""

    delay: float
    """Delay before generating the PDF (in milliseconds)"""

    region: str
    """The desired region for the action to be performed in"""

    use_proxy: Annotated[bool, PropertyInfo(alias="useProxy")]
    """Use a Steel-provided residential proxy for generating the PDF"""
