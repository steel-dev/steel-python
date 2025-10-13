# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProfileCreateResponse",
    "Dimensions",
    "Fingerprint",
    "FingerprintFingerprint",
    "FingerprintFingerprintBattery",
    "FingerprintFingerprintMultimediaDevices",
    "FingerprintFingerprintMultimediaDevicesMicro",
    "FingerprintFingerprintMultimediaDevicesSpeaker",
    "FingerprintFingerprintMultimediaDevicesWebcam",
    "FingerprintFingerprintNavigator",
    "FingerprintFingerprintNavigatorExtraProperties",
    "FingerprintFingerprintNavigatorUserAgentData",
    "FingerprintFingerprintNavigatorUserAgentDataBrand",
    "FingerprintFingerprintPluginsData",
    "FingerprintFingerprintPluginsDataPlugin",
    "FingerprintFingerprintPluginsDataPluginMimeType",
    "FingerprintFingerprintScreen",
    "FingerprintFingerprintVideoCard",
    "FingerprintHeaders",
]


class Dimensions(BaseModel):
    height: float

    width: float


class FingerprintFingerprintBattery(BaseModel):
    charging: Optional[bool] = None

    charging_time: Optional[float] = FieldInfo(alias="chargingTime", default=None)

    discharging_time: Optional[float] = FieldInfo(alias="dischargingTime", default=None)

    level: Optional[float] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintMultimediaDevicesMicro(BaseModel):
    device_id: Optional[str] = FieldInfo(alias="deviceId", default=None)

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    kind: Optional[str] = None

    label: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintMultimediaDevicesSpeaker(BaseModel):
    device_id: Optional[str] = FieldInfo(alias="deviceId", default=None)

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    kind: Optional[str] = None

    label: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintMultimediaDevicesWebcam(BaseModel):
    device_id: Optional[str] = FieldInfo(alias="deviceId", default=None)

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    kind: Optional[str] = None

    label: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintMultimediaDevices(BaseModel):
    micros: List[FingerprintFingerprintMultimediaDevicesMicro]

    speakers: List[FingerprintFingerprintMultimediaDevicesSpeaker]

    webcams: List[FingerprintFingerprintMultimediaDevicesWebcam]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintNavigatorExtraProperties(BaseModel):
    global_privacy_control: Optional[bool] = FieldInfo(alias="globalPrivacyControl", default=None)

    installed_apps: List[Optional[str]] = FieldInfo(alias="installedApps")

    pdf_viewer_enabled: Optional[bool] = FieldInfo(alias="pdfViewerEnabled", default=None)

    vendor_flavors: List[Optional[str]] = FieldInfo(alias="vendorFlavors")

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintNavigatorUserAgentDataBrand(BaseModel):
    brand: Optional[str] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintNavigatorUserAgentData(BaseModel):
    brands: List[FingerprintFingerprintNavigatorUserAgentDataBrand]

    mobile: Optional[bool] = None

    platform: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintNavigator(BaseModel):
    app_code_name: Optional[str] = FieldInfo(alias="appCodeName", default=None)

    app_name: Optional[str] = FieldInfo(alias="appName", default=None)

    app_version: Optional[str] = FieldInfo(alias="appVersion", default=None)

    device_memory: Optional[float] = FieldInfo(alias="deviceMemory", default=None)

    extra_properties: FingerprintFingerprintNavigatorExtraProperties = FieldInfo(alias="extraProperties")

    hardware_concurrency: Optional[float] = FieldInfo(alias="hardwareConcurrency", default=None)

    language: Optional[str] = None

    languages: List[Optional[str]]

    max_touch_points: Optional[float] = FieldInfo(alias="maxTouchPoints", default=None)

    oscpu: Optional[str] = None

    platform: Optional[str] = None

    product: Optional[str] = None

    product_sub: Optional[str] = FieldInfo(alias="productSub", default=None)

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)

    user_agent_data: FingerprintFingerprintNavigatorUserAgentData = FieldInfo(alias="userAgentData")

    vendor: Optional[str] = None

    vendor_sub: Optional[str] = FieldInfo(alias="vendorSub", default=None)

    webdriver: Optional[bool] = None

    do_not_track: Optional[str] = FieldInfo(alias="doNotTrack", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintPluginsDataPluginMimeType(BaseModel):
    description: Optional[str] = None

    enabled_plugin: Optional[str] = FieldInfo(alias="enabledPlugin", default=None)

    suffixes: Optional[str] = None

    type: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintPluginsDataPlugin(BaseModel):
    description: Optional[str] = None

    filename: Optional[str] = None

    mime_types: List[FingerprintFingerprintPluginsDataPluginMimeType] = FieldInfo(alias="mimeTypes")

    name: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintPluginsData(BaseModel):
    mime_types: List[Optional[str]] = FieldInfo(alias="mimeTypes")

    plugins: List[FingerprintFingerprintPluginsDataPlugin]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintScreen(BaseModel):
    avail_height: Optional[float] = FieldInfo(alias="availHeight", default=None)

    avail_left: Optional[float] = FieldInfo(alias="availLeft", default=None)

    avail_top: Optional[float] = FieldInfo(alias="availTop", default=None)

    avail_width: Optional[float] = FieldInfo(alias="availWidth", default=None)

    client_height: Optional[float] = FieldInfo(alias="clientHeight", default=None)

    client_width: Optional[float] = FieldInfo(alias="clientWidth", default=None)

    color_depth: Optional[float] = FieldInfo(alias="colorDepth", default=None)

    device_pixel_ratio: Optional[float] = FieldInfo(alias="devicePixelRatio", default=None)

    has_hdr: Optional[bool] = FieldInfo(alias="hasHDR", default=None)

    height: Optional[float] = None

    inner_height: Optional[float] = FieldInfo(alias="innerHeight", default=None)

    inner_width: Optional[float] = FieldInfo(alias="innerWidth", default=None)

    outer_height: Optional[float] = FieldInfo(alias="outerHeight", default=None)

    outer_width: Optional[float] = FieldInfo(alias="outerWidth", default=None)

    page_x_offset: Optional[float] = FieldInfo(alias="pageXOffset", default=None)

    page_y_offset: Optional[float] = FieldInfo(alias="pageYOffset", default=None)

    pixel_depth: Optional[float] = FieldInfo(alias="pixelDepth", default=None)

    screen_x: Optional[float] = FieldInfo(alias="screenX", default=None)

    width: Optional[float] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprintVideoCard(BaseModel):
    renderer: Optional[str] = None

    vendor: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintFingerprint(BaseModel):
    audio_codecs: Dict[str, Optional[str]] = FieldInfo(alias="audioCodecs")

    battery: FingerprintFingerprintBattery

    fonts: List[Optional[str]]

    mock_web_rtc: Optional[bool] = FieldInfo(alias="mockWebRTC", default=None)

    multimedia_devices: FingerprintFingerprintMultimediaDevices = FieldInfo(alias="multimediaDevices")

    navigator: FingerprintFingerprintNavigator

    plugins_data: FingerprintFingerprintPluginsData = FieldInfo(alias="pluginsData")

    screen: FingerprintFingerprintScreen

    slim: Optional[bool] = None

    video_card: FingerprintFingerprintVideoCard = FieldInfo(alias="videoCard")

    video_codecs: Dict[str, Optional[str]] = FieldInfo(alias="videoCodecs")

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FingerprintHeaders(BaseModel):
    user_agent: Optional[str] = FieldInfo(alias="user-agent", default=None)

    accept: Optional[str] = None

    accept_encoding: Optional[str] = FieldInfo(alias="accept-encoding", default=None)

    accept_language: Optional[str] = FieldInfo(alias="accept-language", default=None)

    dnt: Optional[str] = None

    sec_ch_ua: Optional[str] = FieldInfo(alias="sec-ch-ua", default=None)

    sec_ch_ua_mobile: Optional[str] = FieldInfo(alias="sec-ch-ua-mobile", default=None)

    sec_ch_ua_platform: Optional[str] = FieldInfo(alias="sec-ch-ua-platform", default=None)

    sec_fetch_dest: Optional[str] = FieldInfo(alias="sec-fetch-dest", default=None)

    sec_fetch_mode: Optional[str] = FieldInfo(alias="sec-fetch-mode", default=None)

    sec_fetch_site: Optional[str] = FieldInfo(alias="sec-fetch-site", default=None)

    sec_fetch_user: Optional[str] = FieldInfo(alias="sec-fetch-user", default=None)

    upgrade_insecure_requests: Optional[str] = FieldInfo(alias="upgrade-insecure-requests", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Fingerprint(BaseModel):
    fingerprint: FingerprintFingerprint

    headers: FingerprintHeaders


class ProfileCreateResponse(BaseModel):
    id: str
    """The unique identifier for the profile"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the profile was created"""

    dimensions: Optional[Dimensions] = None
    """The dimensions associated with the profile"""

    extension_ids: Optional[List[str]] = FieldInfo(alias="extensionIds", default=None)
    """The extension IDs associated with the profile"""

    fingerprint: Optional[Fingerprint] = None
    """The fingerprint associated with the profile"""

    source_session_id: Optional[str] = FieldInfo(alias="sourceSessionId", default=None)
    """The last session ID associated with the profile"""

    status: Literal["UPLOADING", "READY", "FAILED"]
    """The status of the profile"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the profile was last updated"""

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)
    """The user agent associated with the profile"""

    credentials_config: Optional[object] = FieldInfo(alias="credentialsConfig", default=None)
    """The credentials configuration associated with the profile"""

    use_proxy_config: Optional[object] = FieldInfo(alias="useProxyConfig", default=None)
    """The proxy configuration associated with the profile"""
