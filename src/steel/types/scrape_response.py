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

    article_author: Optional[str] = FieldInfo(alias="articleAuthor", default=None)
    """Author of the article content"""

    author: Optional[str] = None
    """Author of the webpage content"""

    canonical: Optional[str] = None
    """Canonical URL of the webpage"""

    description: Optional[str] = None
    """Description of the webpage"""

    favicon: Optional[str] = None
    """Favicon URL of the website"""

    json_ld: Optional[object] = FieldInfo(alias="jsonLd", default=None)
    """JSON-LD structured data from the webpage"""

    keywords: Optional[str] = None
    """Keywords associated with the webpage"""

    language: Optional[str] = None
    """Detected language of the webpage"""

    modified_time: Optional[str] = FieldInfo(alias="modifiedTime", default=None)
    """Last modification time of the content"""

    og_description: Optional[str] = FieldInfo(alias="ogDescription", default=None)
    """Open Graph description"""

    og_image: Optional[str] = FieldInfo(alias="ogImage", default=None)
    """Open Graph image URL"""

    og_site_name: Optional[str] = FieldInfo(alias="ogSiteName", default=None)
    """Open Graph site name"""

    og_title: Optional[str] = FieldInfo(alias="ogTitle", default=None)
    """Open Graph title"""

    og_url: Optional[str] = FieldInfo(alias="ogUrl", default=None)
    """Open Graph URL"""

    published_time: Optional[str] = FieldInfo(alias="publishedTime", default=None)
    """Publication time of the content"""

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
