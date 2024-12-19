# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScrapeResponse", "Content", "Link", "Metadata", "Pdf", "Screenshot"]


class Content(BaseModel):
    cleaned_html: Optional[str] = None
    """Cleaned HTML content of the webpage"""

    html: Optional[str] = None
    """Raw HTML content of the webpage"""

    markdown: Optional[str] = None
    """Webpage content converted to Markdown"""

    readability: Optional[Dict[str, object]] = None
    """Webpage content in Readability format"""


class Link(BaseModel):
    text: str
    """Text content of the link"""

    url: str
    """URL of the link"""


class Metadata(BaseModel):
    status_code: int = FieldInfo(alias="statusCode")
    """HTTP status code of the response"""

    description: Optional[str] = None
    """Description of the webpage"""

    language: Optional[str] = None
    """Detected language of the webpage"""

    og_description: Optional[str] = FieldInfo(alias="ogDescription", default=None)
    """Open Graph description"""

    og_image: Optional[str] = FieldInfo(alias="ogImage", default=None)
    """Open Graph image URL"""

    og_title: Optional[str] = FieldInfo(alias="ogTitle", default=None)
    """Open Graph title"""

    published_timestamp: Optional[datetime] = None
    """Publication timestamp of the content (if available)"""

    timestamp: Optional[datetime] = None
    """Timestamp when the scrape was performed"""

    title: Optional[str] = None
    """Title of the webpage"""

    url_source: Optional[str] = FieldInfo(alias="urlSource", default=None)
    """Source URL of the scraped page"""


class Pdf(BaseModel):
    url: str
    """URL of the generated PDF"""


class Screenshot(BaseModel):
    url: str
    """URL of the screenshot image"""


class ScrapeResponse(BaseModel):
    content: Content

    links: List[Link]

    metadata: Metadata

    pdf: Optional[Pdf] = None

    screenshot: Optional[Screenshot] = None
