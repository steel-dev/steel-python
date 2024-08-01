# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ScrapeResponse"]


class ScrapeResponse(BaseModel):
    cleaned_html: Optional[str] = None
    """The cleaned HTML content of the scraped webpage"""

    html: Optional[str] = None
    """The raw HTML content of the scraped webpage"""

    markdown: Optional[str] = None
    """The content of the webpage converted to Markdown format"""

    readability: Optional[object] = None
    """The readable content extracted from the webpage"""
