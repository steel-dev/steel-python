# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TopLevelScrapeParams"]


class TopLevelScrapeParams(TypedDict, total=False):
    url: Required[str]
    """The URL of the webpage to scrape"""

    orgid: Required[str]

    format: List[Literal["html", "cleaned_html", "readability", "markdown"]]
    """The desired format(s) for the scraped content"""
