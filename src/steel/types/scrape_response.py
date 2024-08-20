# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScrapeResponse", "Content", "Link", "Metadata", "Pdf", "Screenshot"]


class Content(BaseModel):
    cleaned_html: Optional[str] = None
    """The cleaned HTML content of the scraped webpage"""

    html: Optional[str] = None
    """The raw HTML content of the scraped webpage"""

    markdown: Optional[str] = None
    """The content of the webpage converted to Markdown format"""


class Link(BaseModel):
    text: Optional[str] = None
    """The text content of the link"""

    url: Optional[str] = None
    """The URL of the link"""


class Metadata(BaseModel):
    description: Optional[str] = None
    """The description of the webpage"""

    language: Optional[str] = None
    """The detected language of the webpage"""

    og_description: Optional[str] = FieldInfo(alias="ogDescription", default=None)
    """The Open Graph description"""

    og_image: Optional[str] = FieldInfo(alias="ogImage", default=None)
    """The Open Graph image URL"""

    og_title: Optional[str] = FieldInfo(alias="ogTitle", default=None)
    """The Open Graph title"""

    published_timestamp: Optional[datetime] = None
    """The timestamp of when the content was published (if available)"""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """The HTTP status code of the response"""

    timestamp: Optional[datetime] = None
    """The timestamp of when the scrape was performed"""

    title: Optional[str] = None
    """The title of the webpage"""

    url_source: Optional[str] = FieldInfo(alias="urlSource", default=None)
    """The source URL of the scraped page"""


class Pdf(BaseModel):
    url: Optional[str] = None
    """The URL of the generated PDF"""


class Screenshot(BaseModel):
    url: Optional[str] = None
    """The URL of the screenshot image"""


class ScrapeResponse(BaseModel):
    content: Optional[Content] = None

    links: Optional[List[Link]] = None

    metadata: Optional[Metadata] = None

    pdf: Optional[Pdf] = None

    screenshot: Optional[Screenshot] = None
