# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionContext", "Cookie"]


class Cookie(BaseModel):
    name: str
    """The name of the cookie"""

    value: str
    """The value of the cookie"""

    domain: Optional[str] = None
    """The domain of the cookie"""

    expires: Optional[float] = None
    """The expiration date of the cookie"""

    http_only: Optional[bool] = FieldInfo(alias="httpOnly", default=None)
    """Whether the cookie is HTTP only"""

    partition_key: Optional[str] = FieldInfo(alias="partitionKey", default=None)
    """The partition key of the cookie"""

    path: Optional[str] = None
    """The path of the cookie"""

    priority: Optional[Literal["Low", "Medium", "High"]] = None
    """The priority of the cookie"""

    same_party: Optional[bool] = FieldInfo(alias="sameParty", default=None)
    """Whether the cookie is a same party cookie"""

    same_site: Optional[Literal["Strict", "Lax", "None"]] = FieldInfo(alias="sameSite", default=None)
    """The same site attribute of the cookie"""

    secure: Optional[bool] = None
    """Whether the cookie is secure"""

    session: Optional[bool] = None
    """Whether the cookie is a session cookie"""

    size: Optional[float] = None
    """The size of the cookie"""

    source_port: Optional[float] = FieldInfo(alias="sourcePort", default=None)
    """The source port of the cookie"""

    source_scheme: Optional[Literal["Unset", "NonSecure", "Secure"]] = FieldInfo(alias="sourceScheme", default=None)
    """The source scheme of the cookie"""

    url: Optional[str] = None
    """The URL of the cookie"""


class SessionContext(BaseModel):
    cookies: Optional[List[Cookie]] = None
    """Cookies to initialize in the session"""

    indexed_db: Optional[Dict[str, List[Dict[str, object]]]] = FieldInfo(alias="indexedDB", default=None)
    """Domain-specific indexedDB items to initialize in the session"""

    local_storage: Optional[Dict[str, Dict[str, object]]] = FieldInfo(alias="localStorage", default=None)
    """Domain-specific localStorage items to initialize in the session"""

    session_storage: Optional[Dict[str, Dict[str, object]]] = FieldInfo(alias="sessionStorage", default=None)
    """Domain-specific sessionStorage items to initialize in the session"""
