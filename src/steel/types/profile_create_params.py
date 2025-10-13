# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ProfileCreateParams",
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
    "Dimensions",
]


class ProfileCreateParams(TypedDict, total=False):
    fingerprint: Required[Optional[Fingerprint]]
    """The fingerprint associated with the profile"""

    proxy_url: Required[Annotated[Optional[str], PropertyInfo(alias="proxyUrl")]]
    """The proxy associated with the profile"""

    user_agent: Required[Annotated[Optional[str], PropertyInfo(alias="userAgent")]]
    """The user agent associated with the profile"""

    dimensions: Dimensions
    """The dimensions associated with the profile"""

    user_data_dir: Annotated[object, PropertyInfo(alias="userDataDir")]
    """The user data directory associated with the profile"""


class FingerprintFingerprintBatteryTyped(TypedDict, total=False):
    charging: Required[Optional[bool]]

    charging_time: Required[Annotated[Optional[float], PropertyInfo(alias="chargingTime")]]

    discharging_time: Required[Annotated[Optional[float], PropertyInfo(alias="dischargingTime")]]

    level: Required[Optional[float]]


FingerprintFingerprintBattery: TypeAlias = Union[FingerprintFingerprintBatteryTyped, Dict[str, object]]


class FingerprintFingerprintMultimediaDevicesMicroTyped(TypedDict, total=False):
    device_id: Required[Annotated[Optional[str], PropertyInfo(alias="deviceId")]]

    group_id: Required[Annotated[Optional[str], PropertyInfo(alias="groupId")]]

    kind: Required[Optional[str]]

    label: Required[Optional[str]]


FingerprintFingerprintMultimediaDevicesMicro: TypeAlias = Union[
    FingerprintFingerprintMultimediaDevicesMicroTyped, Dict[str, object]
]


class FingerprintFingerprintMultimediaDevicesSpeakerTyped(TypedDict, total=False):
    device_id: Required[Annotated[Optional[str], PropertyInfo(alias="deviceId")]]

    group_id: Required[Annotated[Optional[str], PropertyInfo(alias="groupId")]]

    kind: Required[Optional[str]]

    label: Required[Optional[str]]


FingerprintFingerprintMultimediaDevicesSpeaker: TypeAlias = Union[
    FingerprintFingerprintMultimediaDevicesSpeakerTyped, Dict[str, object]
]


class FingerprintFingerprintMultimediaDevicesWebcamTyped(TypedDict, total=False):
    device_id: Required[Annotated[Optional[str], PropertyInfo(alias="deviceId")]]

    group_id: Required[Annotated[Optional[str], PropertyInfo(alias="groupId")]]

    kind: Required[Optional[str]]

    label: Required[Optional[str]]


FingerprintFingerprintMultimediaDevicesWebcam: TypeAlias = Union[
    FingerprintFingerprintMultimediaDevicesWebcamTyped, Dict[str, object]
]


class FingerprintFingerprintMultimediaDevicesTyped(TypedDict, total=False):
    micros: Required[Iterable[FingerprintFingerprintMultimediaDevicesMicro]]

    speakers: Required[Iterable[FingerprintFingerprintMultimediaDevicesSpeaker]]

    webcams: Required[Iterable[FingerprintFingerprintMultimediaDevicesWebcam]]


FingerprintFingerprintMultimediaDevices: TypeAlias = Union[
    FingerprintFingerprintMultimediaDevicesTyped, Dict[str, object]
]


class FingerprintFingerprintNavigatorExtraPropertiesTyped(TypedDict, total=False):
    global_privacy_control: Required[Annotated[Optional[bool], PropertyInfo(alias="globalPrivacyControl")]]

    installed_apps: Required[Annotated[SequenceNotStr[Optional[str]], PropertyInfo(alias="installedApps")]]

    pdf_viewer_enabled: Required[Annotated[Optional[bool], PropertyInfo(alias="pdfViewerEnabled")]]

    vendor_flavors: Required[Annotated[SequenceNotStr[Optional[str]], PropertyInfo(alias="vendorFlavors")]]


FingerprintFingerprintNavigatorExtraProperties: TypeAlias = Union[
    FingerprintFingerprintNavigatorExtraPropertiesTyped, Dict[str, object]
]


class FingerprintFingerprintNavigatorUserAgentDataBrandTyped(TypedDict, total=False):
    brand: Required[Optional[str]]

    version: Required[Optional[str]]


FingerprintFingerprintNavigatorUserAgentDataBrand: TypeAlias = Union[
    FingerprintFingerprintNavigatorUserAgentDataBrandTyped, Dict[str, object]
]


class FingerprintFingerprintNavigatorUserAgentDataTyped(TypedDict, total=False):
    brands: Required[Iterable[FingerprintFingerprintNavigatorUserAgentDataBrand]]

    mobile: Required[Optional[bool]]

    platform: Required[Optional[str]]


FingerprintFingerprintNavigatorUserAgentData: TypeAlias = Union[
    FingerprintFingerprintNavigatorUserAgentDataTyped, Dict[str, object]
]


class FingerprintFingerprintNavigatorTyped(TypedDict, total=False):
    app_code_name: Required[Annotated[Optional[str], PropertyInfo(alias="appCodeName")]]

    app_name: Required[Annotated[Optional[str], PropertyInfo(alias="appName")]]

    app_version: Required[Annotated[Optional[str], PropertyInfo(alias="appVersion")]]

    device_memory: Required[Annotated[Optional[float], PropertyInfo(alias="deviceMemory")]]

    extra_properties: Required[
        Annotated[FingerprintFingerprintNavigatorExtraProperties, PropertyInfo(alias="extraProperties")]
    ]

    hardware_concurrency: Required[Annotated[Optional[float], PropertyInfo(alias="hardwareConcurrency")]]

    language: Required[Optional[str]]

    languages: Required[SequenceNotStr[Optional[str]]]

    max_touch_points: Required[Annotated[Optional[float], PropertyInfo(alias="maxTouchPoints")]]

    oscpu: Required[Optional[str]]

    platform: Required[Optional[str]]

    product: Required[Optional[str]]

    product_sub: Required[Annotated[Optional[str], PropertyInfo(alias="productSub")]]

    user_agent: Required[Annotated[Optional[str], PropertyInfo(alias="userAgent")]]

    user_agent_data: Required[
        Annotated[FingerprintFingerprintNavigatorUserAgentData, PropertyInfo(alias="userAgentData")]
    ]

    vendor: Required[Optional[str]]

    vendor_sub: Required[Annotated[Optional[str], PropertyInfo(alias="vendorSub")]]

    webdriver: Required[Optional[bool]]

    do_not_track: Annotated[Optional[str], PropertyInfo(alias="doNotTrack")]


FingerprintFingerprintNavigator: TypeAlias = Union[FingerprintFingerprintNavigatorTyped, Dict[str, object]]


class FingerprintFingerprintPluginsDataPluginMimeTypeTyped(TypedDict, total=False):
    description: Required[Optional[str]]

    enabled_plugin: Required[Annotated[Optional[str], PropertyInfo(alias="enabledPlugin")]]

    suffixes: Required[Optional[str]]

    type: Required[Optional[str]]


FingerprintFingerprintPluginsDataPluginMimeType: TypeAlias = Union[
    FingerprintFingerprintPluginsDataPluginMimeTypeTyped, Dict[str, object]
]


class FingerprintFingerprintPluginsDataPluginTyped(TypedDict, total=False):
    description: Required[Optional[str]]

    filename: Required[Optional[str]]

    mime_types: Required[
        Annotated[Iterable[FingerprintFingerprintPluginsDataPluginMimeType], PropertyInfo(alias="mimeTypes")]
    ]

    name: Required[Optional[str]]


FingerprintFingerprintPluginsDataPlugin: TypeAlias = Union[
    FingerprintFingerprintPluginsDataPluginTyped, Dict[str, object]
]


class FingerprintFingerprintPluginsDataTyped(TypedDict, total=False):
    mime_types: Required[Annotated[SequenceNotStr[Optional[str]], PropertyInfo(alias="mimeTypes")]]

    plugins: Required[Iterable[FingerprintFingerprintPluginsDataPlugin]]


FingerprintFingerprintPluginsData: TypeAlias = Union[FingerprintFingerprintPluginsDataTyped, Dict[str, object]]


class FingerprintFingerprintScreenTyped(TypedDict, total=False):
    avail_height: Required[Annotated[Optional[float], PropertyInfo(alias="availHeight")]]

    avail_left: Required[Annotated[Optional[float], PropertyInfo(alias="availLeft")]]

    avail_top: Required[Annotated[Optional[float], PropertyInfo(alias="availTop")]]

    avail_width: Required[Annotated[Optional[float], PropertyInfo(alias="availWidth")]]

    client_height: Required[Annotated[Optional[float], PropertyInfo(alias="clientHeight")]]

    client_width: Required[Annotated[Optional[float], PropertyInfo(alias="clientWidth")]]

    color_depth: Required[Annotated[Optional[float], PropertyInfo(alias="colorDepth")]]

    device_pixel_ratio: Required[Annotated[Optional[float], PropertyInfo(alias="devicePixelRatio")]]

    has_hdr: Required[Annotated[Optional[bool], PropertyInfo(alias="hasHDR")]]

    height: Required[Optional[float]]

    inner_height: Required[Annotated[Optional[float], PropertyInfo(alias="innerHeight")]]

    inner_width: Required[Annotated[Optional[float], PropertyInfo(alias="innerWidth")]]

    outer_height: Required[Annotated[Optional[float], PropertyInfo(alias="outerHeight")]]

    outer_width: Required[Annotated[Optional[float], PropertyInfo(alias="outerWidth")]]

    page_x_offset: Required[Annotated[Optional[float], PropertyInfo(alias="pageXOffset")]]

    page_y_offset: Required[Annotated[Optional[float], PropertyInfo(alias="pageYOffset")]]

    pixel_depth: Required[Annotated[Optional[float], PropertyInfo(alias="pixelDepth")]]

    screen_x: Required[Annotated[Optional[float], PropertyInfo(alias="screenX")]]

    width: Required[Optional[float]]


FingerprintFingerprintScreen: TypeAlias = Union[FingerprintFingerprintScreenTyped, Dict[str, object]]


class FingerprintFingerprintVideoCardTyped(TypedDict, total=False):
    renderer: Required[Optional[str]]

    vendor: Required[Optional[str]]


FingerprintFingerprintVideoCard: TypeAlias = Union[FingerprintFingerprintVideoCardTyped, Dict[str, object]]


class FingerprintFingerprintTyped(TypedDict, total=False):
    audio_codecs: Required[Annotated[Dict[str, Optional[str]], PropertyInfo(alias="audioCodecs")]]

    battery: Required[FingerprintFingerprintBattery]

    fonts: Required[SequenceNotStr[Optional[str]]]

    mock_web_rtc: Required[Annotated[Optional[bool], PropertyInfo(alias="mockWebRTC")]]

    multimedia_devices: Required[
        Annotated[FingerprintFingerprintMultimediaDevices, PropertyInfo(alias="multimediaDevices")]
    ]

    navigator: Required[FingerprintFingerprintNavigator]

    plugins_data: Required[Annotated[FingerprintFingerprintPluginsData, PropertyInfo(alias="pluginsData")]]

    screen: Required[FingerprintFingerprintScreen]

    slim: Required[Optional[bool]]

    video_card: Required[Annotated[FingerprintFingerprintVideoCard, PropertyInfo(alias="videoCard")]]

    video_codecs: Required[Annotated[Dict[str, Optional[str]], PropertyInfo(alias="videoCodecs")]]


FingerprintFingerprint: TypeAlias = Union[FingerprintFingerprintTyped, Dict[str, object]]


class FingerprintHeadersTyped(TypedDict, total=False):
    user_agent: Required[Annotated[Optional[str], PropertyInfo(alias="user-agent")]]

    accept: Optional[str]

    accept_encoding: Annotated[Optional[str], PropertyInfo(alias="accept-encoding")]

    accept_language: Annotated[Optional[str], PropertyInfo(alias="accept-language")]

    dnt: Optional[str]

    sec_ch_ua: Annotated[Optional[str], PropertyInfo(alias="sec-ch-ua")]

    sec_ch_ua_mobile: Annotated[Optional[str], PropertyInfo(alias="sec-ch-ua-mobile")]

    sec_ch_ua_platform: Annotated[Optional[str], PropertyInfo(alias="sec-ch-ua-platform")]

    sec_fetch_dest: Annotated[Optional[str], PropertyInfo(alias="sec-fetch-dest")]

    sec_fetch_mode: Annotated[Optional[str], PropertyInfo(alias="sec-fetch-mode")]

    sec_fetch_site: Annotated[Optional[str], PropertyInfo(alias="sec-fetch-site")]

    sec_fetch_user: Annotated[Optional[str], PropertyInfo(alias="sec-fetch-user")]

    upgrade_insecure_requests: Annotated[Optional[str], PropertyInfo(alias="upgrade-insecure-requests")]


FingerprintHeaders: TypeAlias = Union[FingerprintHeadersTyped, Dict[str, object]]


class Fingerprint(TypedDict, total=False):
    fingerprint: Required[FingerprintFingerprint]

    headers: Required[FingerprintHeaders]


class Dimensions(TypedDict, total=False):
    height: Required[float]

    width: Required[float]
