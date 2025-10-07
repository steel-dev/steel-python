# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientScrapeParams"]


class ClientScrapeParams(TypedDict, total=False):
    url: Required[str]
    """URL of the webpage to scrape"""

    delay: float
    """Delay before scraping (in milliseconds)"""

    format: List[Literal["html", "readability", "cleaned_html", "markdown"]]
    """Desired format(s) for the scraped content. Default is `html`."""

    pdf: bool
    """Include a PDF in the response"""

    region: str
    """The desired region for the action to be performed in"""

    screenshot: bool
    """Include a screenshot in the response"""

    use_proxy: Annotated[bool, PropertyInfo(alias="useProxy")]
    """Use a Steel-provided residential proxy for the scrape"""
