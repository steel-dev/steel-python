# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionContext", "Cookie"]


class Cookie(BaseModel):
    domain: str
    """Domain the cookie belongs to"""

    name: str
    """Name of the cookie"""

    value: str
    """Value of the cookie"""

    expires: Optional[float] = None
    """Unix timestamp when the cookie expires"""

    http_only: Optional[bool] = FieldInfo(alias="httpOnly", default=None)
    """Whether the cookie is HTTP only"""

    path: Optional[str] = None
    """Path the cookie is valid for"""

    same_site: Optional[Literal["Strict", "Lax", "None"]] = FieldInfo(alias="sameSite", default=None)
    """SameSite attribute of the cookie"""

    secure: Optional[bool] = None
    """Whether the cookie requires HTTPS"""


class SessionContext(BaseModel):
    cookies: Optional[List[Cookie]] = None
    """Cookies from the session"""

    local_storage: Optional[Dict[str, Dict[str, object]]] = FieldInfo(alias="localStorage", default=None)
    """Local storage items from the session"""
