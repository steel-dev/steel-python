# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CaptchaStatusResponse", "CaptchaStatusResponseItem"]


class CaptchaStatusResponseItem(BaseModel):
    is_solving_captcha: bool = FieldInfo(alias="isSolvingCaptcha")
    """Whether a captcha is currently being solved"""

    page_id: str = FieldInfo(alias="pageId")
    """The page ID where the captcha is located"""

    tasks: List[object]
    """Array of captcha tasks"""

    url: str
    """The URL where the captcha is located"""

    created: Optional[float] = None
    """Timestamp when the state was created"""

    last_updated: Optional[float] = FieldInfo(alias="lastUpdated", default=None)
    """Timestamp when the state was last updated"""


CaptchaStatusResponse: TypeAlias = List[CaptchaStatusResponseItem]
