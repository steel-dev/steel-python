# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SessionCreateParams",
    "Credentials",
    "DeviceConfig",
    "Dimensions",
    "OptimizeBandwidth",
    "OptimizeBandwidthUnionMember1",
    "SessionContext",
    "SessionContextCookie",
    "SessionContextCookiePartitionKey",
    "SessionContextIndexedDB",
    "SessionContextIndexedDBData",
    "SessionContextIndexedDBDataRecord",
    "SessionContextIndexedDBDataRecordBlobFile",
    "StealthConfig",
    "UseProxy",
    "UseProxyGeolocation",
    "UseProxyGeolocationGeolocation",
    "UseProxyServer",
]


class SessionCreateParams(TypedDict, total=False):
    block_ads: Annotated[bool, PropertyInfo(alias="blockAds")]
    """Block ads in the browser session. Default is false."""

    concurrency: int
    """Number of sessions to create concurrently (check your plan limit)"""

    credentials: Credentials
    """Configuration for session credentials"""

    device_config: Annotated[DeviceConfig, PropertyInfo(alias="deviceConfig")]
    """Device configuration for the session.

    Specify 'mobile' for mobile device fingerprints and configurations.
    """

    dimensions: Dimensions
    """Viewport and browser window dimensions for the session"""

    extension_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="extensionIds")]
    """Array of extension IDs to install in the session.

    Use ['all_ext'] to install all uploaded extensions.
    """

    headless: bool
    """Enable headless browser mode (disable Headful mode)"""

    is_selenium: Annotated[bool, PropertyInfo(alias="isSelenium")]
    """Enable Selenium mode for the browser session (default is false).

    Use this when you plan to connect to the browser session via Selenium.
    """

    namespace: str
    """The namespace the session should be created against. Defaults to "default"."""

    optimize_bandwidth: Annotated[OptimizeBandwidth, PropertyInfo(alias="optimizeBandwidth")]
    """Enable bandwidth optimizations.

    Passing true enables all flags (except hosts/patterns). Object allows granular
    control.
    """

    persist_profile: Annotated[bool, PropertyInfo(alias="persistProfile")]
    """This flag will persist the user profile for the session."""

    profile_id: Annotated[str, PropertyInfo(alias="profileId")]
    """This flag will set the profile for the session."""

    proxy_url: Annotated[str, PropertyInfo(alias="proxyUrl")]
    """Custom proxy URL for the browser session.

    Overrides useProxy, disabling Steel-provided proxies in favor of your specified
    proxy. Format: http(s)://username:password@hostname:port
    """

    region: str
    """The desired region for the session to be started in.

    Available regions are lax, ord, iad
    """

    session_context: Annotated[SessionContext, PropertyInfo(alias="sessionContext")]
    """Session context data to be used in the created session.

    Sessions will start with an empty context by default.
    """

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Optional custom UUID for the session"""

    solve_captcha: Annotated[bool, PropertyInfo(alias="solveCaptcha")]
    """Enable automatic captcha solving. Default is false."""

    stealth_config: Annotated[StealthConfig, PropertyInfo(alias="stealthConfig")]
    """Stealth configuration for the session"""

    api_timeout: Annotated[int, PropertyInfo(alias="timeout")]
    """Session timeout duration in milliseconds. Default is 300000 (5 minutes)."""

    use_proxy: Annotated[UseProxy, PropertyInfo(alias="useProxy")]
    """Proxy configuration for the session.

    Can be a boolean or array of proxy configurations
    """

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]
    """Custom user agent string for the browser session"""


class Credentials(TypedDict, total=False):
    auto_submit: Annotated[bool, PropertyInfo(alias="autoSubmit")]

    blur_fields: Annotated[bool, PropertyInfo(alias="blurFields")]

    exact_origin: Annotated[bool, PropertyInfo(alias="exactOrigin")]


class DeviceConfig(TypedDict, total=False):
    device: Literal["desktop", "mobile"]


class Dimensions(TypedDict, total=False):
    height: Required[int]
    """Height of the session"""

    width: Required[int]
    """Width of the session"""


class OptimizeBandwidthUnionMember1(TypedDict, total=False):
    block_hosts: Annotated[SequenceNotStr[str], PropertyInfo(alias="blockHosts")]

    block_images: Annotated[bool, PropertyInfo(alias="blockImages")]

    block_media: Annotated[bool, PropertyInfo(alias="blockMedia")]

    block_stylesheets: Annotated[bool, PropertyInfo(alias="blockStylesheets")]

    block_url_patterns: Annotated[SequenceNotStr[str], PropertyInfo(alias="blockUrlPatterns")]


OptimizeBandwidth: TypeAlias = Union[bool, OptimizeBandwidthUnionMember1]


class SessionContextCookiePartitionKey(TypedDict, total=False):
    has_cross_site_ancestor: Required[Annotated[bool, PropertyInfo(alias="hasCrossSiteAncestor")]]
    """
    Indicates if the cookie has any ancestors that are cross-site to the
    topLevelSite.
    """

    top_level_site: Required[Annotated[str, PropertyInfo(alias="topLevelSite")]]
    """
    The site of the top-level URL the browser was visiting at the start of the
    request to the endpoint that set the cookie.
    """


class SessionContextCookie(TypedDict, total=False):
    name: Required[str]
    """The name of the cookie"""

    value: Required[str]
    """The value of the cookie"""

    domain: str
    """The domain of the cookie"""

    expires: float
    """The expiration date of the cookie"""

    http_only: Annotated[bool, PropertyInfo(alias="httpOnly")]
    """Whether the cookie is HTTP only"""

    partition_key: Annotated[SessionContextCookiePartitionKey, PropertyInfo(alias="partitionKey")]
    """The partition key of the cookie"""

    path: str
    """The path of the cookie"""

    priority: Literal["Low", "Medium", "High"]
    """The priority of the cookie"""

    same_party: Annotated[bool, PropertyInfo(alias="sameParty")]
    """Whether the cookie is a same party cookie"""

    same_site: Annotated[Literal["Strict", "Lax", "None"], PropertyInfo(alias="sameSite")]
    """The same site attribute of the cookie"""

    secure: bool
    """Whether the cookie is secure"""

    session: bool
    """Whether the cookie is a session cookie"""

    size: float
    """The size of the cookie"""

    source_port: Annotated[float, PropertyInfo(alias="sourcePort")]
    """The source port of the cookie"""

    source_scheme: Annotated[Literal["Unset", "NonSecure", "Secure"], PropertyInfo(alias="sourceScheme")]
    """The source scheme of the cookie"""

    url: str
    """The URL of the cookie"""


class SessionContextIndexedDBDataRecordBlobFile(TypedDict, total=False):
    blob_number: Required[Annotated[float, PropertyInfo(alias="blobNumber")]]

    mime_type: Required[Annotated[str, PropertyInfo(alias="mimeType")]]

    size: Required[float]

    filename: str

    last_modified: Annotated[Union[str, datetime], PropertyInfo(alias="lastModified", format="iso8601")]

    path: str


class SessionContextIndexedDBDataRecord(TypedDict, total=False):
    blob_files: Annotated[Iterable[SessionContextIndexedDBDataRecordBlobFile], PropertyInfo(alias="blobFiles")]

    key: object

    value: object


class SessionContextIndexedDBData(TypedDict, total=False):
    id: Required[float]

    name: Required[str]

    records: Required[Iterable[SessionContextIndexedDBDataRecord]]


class SessionContextIndexedDB(TypedDict, total=False):
    id: Required[float]

    data: Required[Iterable[SessionContextIndexedDBData]]

    name: Required[str]


class SessionContext(TypedDict, total=False):
    cookies: Iterable[SessionContextCookie]
    """Cookies to initialize in the session"""

    indexed_db: Annotated[Dict[str, Iterable[SessionContextIndexedDB]], PropertyInfo(alias="indexedDB")]
    """Domain-specific indexedDB items to initialize in the session"""

    local_storage: Annotated[Dict[str, Dict[str, str]], PropertyInfo(alias="localStorage")]
    """Domain-specific localStorage items to initialize in the session"""

    session_storage: Annotated[Dict[str, Dict[str, str]], PropertyInfo(alias="sessionStorage")]
    """Domain-specific sessionStorage items to initialize in the session"""


class StealthConfig(TypedDict, total=False):
    humanize_interactions: Annotated[bool, PropertyInfo(alias="humanizeInteractions")]
    """
    This flag will make the browser act more human-like by moving the mouse in a
    more natural way.
    """

    skip_fingerprint_injection: Annotated[bool, PropertyInfo(alias="skipFingerprintInjection")]
    """This flag will skip the fingerprint generation for the session."""


class UseProxyGeolocationGeolocation(TypedDict, total=False):
    country: Required[
        Literal[
            "US",
            "CA",
            "MX",
            "GB",
            "DE",
            "FR",
            "IT",
            "ES",
            "PL",
            "NL",
            "SE",
            "NO",
            "DK",
            "FI",
            "CH",
            "AT",
            "BE",
            "IE",
            "PT",
            "GR",
            "CZ",
            "HU",
            "RO",
            "BG",
            "SK",
            "SI",
            "HR",
            "EE",
            "LV",
            "LT",
            "LU",
            "MT",
            "CY",
            "IS",
            "LI",
            "MC",
            "SM",
            "VA",
            "JP",
            "KR",
            "CN",
            "HK",
            "TW",
            "SG",
            "AU",
            "NZ",
            "IN",
            "TH",
            "MY",
            "PH",
            "ID",
            "VN",
            "AF",
            "BD",
            "BN",
            "KH",
            "LA",
            "LK",
            "MM",
            "NP",
            "PK",
            "FJ",
            "PG",
            "AE",
            "SA",
            "IL",
            "TR",
            "IR",
            "IQ",
            "JO",
            "KW",
            "LB",
            "OM",
            "QA",
            "BH",
            "YE",
            "SY",
            "ZA",
            "EG",
            "MA",
            "NG",
            "KE",
            "DZ",
            "AO",
            "BW",
            "ET",
            "GH",
            "CI",
            "LY",
            "MZ",
            "RW",
            "SN",
            "TN",
            "UG",
            "ZM",
            "ZW",
            "TZ",
            "MU",
            "SC",
            "BR",
            "AR",
            "CL",
            "CO",
            "PE",
            "VE",
            "EC",
            "UY",
            "PY",
            "BO",
            "CR",
            "CU",
            "DO",
            "GT",
            "HN",
            "JM",
            "NI",
            "PA",
            "SV",
            "TT",
            "BB",
            "BZ",
            "GY",
            "SR",
            "RU",
            "UA",
            "BY",
            "KZ",
            "UZ",
            "AZ",
            "GE",
            "AM",
            "MD",
            "MK",
            "AL",
            "BA",
            "RS",
            "ME",
            "XK",
            "MN",
            "KG",
            "TJ",
            "TM",
        ]
    ]
    """Country code (e.g., 'US', 'GB', 'DE') - ISO 3166-1 alpha-2"""

    city: str
    """City name - English name (e.g., 'New York', 'Los Angeles')"""

    state: Literal[
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
        "DC",
        "PR",
        "GU",
        "VI",
    ]
    """State code (e.g., 'NY', 'CA') - US states only"""


class UseProxyGeolocation(TypedDict, total=False):
    geolocation: Required[UseProxyGeolocationGeolocation]
    """Geographic location for the proxy"""


class UseProxyServer(TypedDict, total=False):
    server: Required[str]
    """Proxy server URL"""


UseProxy: TypeAlias = Union[bool, UseProxyGeolocation, UseProxyServer, object]
