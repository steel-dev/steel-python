# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionLiveDetailsResponse", "Page"]


class Page(BaseModel):
    id: str

    favicon: Optional[str] = None

    session_viewer_fullscreen_url: str = FieldInfo(alias="sessionViewerFullscreenUrl")

    session_viewer_url: str = FieldInfo(alias="sessionViewerUrl")

    title: str

    url: str


class SessionLiveDetailsResponse(BaseModel):
    pages: List[Page]

    session_viewer_fullscreen_url: str = FieldInfo(alias="sessionViewerFullscreenUrl")

    session_viewer_url: str = FieldInfo(alias="sessionViewerUrl")

    ws_url: str = FieldInfo(alias="wsUrl")
