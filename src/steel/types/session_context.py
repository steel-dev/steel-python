# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SessionContext",
    "Cookie",
    "CookiePartitionKey",
    "IndexedDB",
    "IndexedDBData",
    "IndexedDBDataRecord",
    "IndexedDBDataRecordBlobFile",
]


class CookiePartitionKey(BaseModel):
    has_cross_site_ancestor: bool = FieldInfo(alias="hasCrossSiteAncestor")
    """
    Indicates if the cookie has any ancestors that are cross-site to the
    topLevelSite.
    """

    top_level_site: str = FieldInfo(alias="topLevelSite")
    """
    The site of the top-level URL the browser was visiting at the start of the
    request to the endpoint that set the cookie.
    """


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

    partition_key: Optional[CookiePartitionKey] = FieldInfo(alias="partitionKey", default=None)
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


class IndexedDBDataRecordBlobFile(BaseModel):
    blob_number: float = FieldInfo(alias="blobNumber")

    mime_type: str = FieldInfo(alias="mimeType")

    size: float

    filename: Optional[str] = None

    last_modified: Optional[datetime] = FieldInfo(alias="lastModified", default=None)

    path: Optional[str] = None


class IndexedDBDataRecord(BaseModel):
    blob_files: Optional[List[IndexedDBDataRecordBlobFile]] = FieldInfo(alias="blobFiles", default=None)

    key: Optional[object] = None

    value: Optional[object] = None


class IndexedDBData(BaseModel):
    id: float

    name: str

    records: List[IndexedDBDataRecord]


class IndexedDB(BaseModel):
    id: float

    data: List[IndexedDBData]

    name: str


class SessionContext(BaseModel):
    cookies: Optional[List[Cookie]] = None
    """Cookies to initialize in the session"""

    indexed_db: Optional[Dict[str, List[IndexedDB]]] = FieldInfo(alias="indexedDB", default=None)
    """Domain-specific indexedDB items to initialize in the session"""

    local_storage: Optional[Dict[str, Dict[str, str]]] = FieldInfo(alias="localStorage", default=None)
    """Domain-specific localStorage items to initialize in the session"""

    session_storage: Optional[Dict[str, Dict[str, str]]] = FieldInfo(alias="sessionStorage", default=None)
    """Domain-specific sessionStorage items to initialize in the session"""
