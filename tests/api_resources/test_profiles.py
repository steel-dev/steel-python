# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import ProfileListResponse, ProfileCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Steel) -> None:
        profile = client.profiles.create(
            fingerprint={
                "fingerprint": {
                    "audio_codecs": {"foo": "string"},
                    "battery": {
                        "charging": True,
                        "charging_time": 0,
                        "discharging_time": 0,
                        "level": 0,
                    },
                    "fonts": ["string"],
                    "mock_web_rtc": True,
                    "multimedia_devices": {
                        "micros": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "speakers": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "webcams": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                    },
                    "navigator": {
                        "app_code_name": "appCodeName",
                        "app_name": "appName",
                        "app_version": "appVersion",
                        "device_memory": 0,
                        "extra_properties": {
                            "global_privacy_control": True,
                            "installed_apps": ["string"],
                            "pdf_viewer_enabled": True,
                            "vendor_flavors": ["string"],
                        },
                        "hardware_concurrency": 0,
                        "language": "language",
                        "languages": ["string"],
                        "max_touch_points": 0,
                        "oscpu": "oscpu",
                        "platform": "platform",
                        "product": "product",
                        "product_sub": "productSub",
                        "user_agent": "userAgent",
                        "user_agent_data": {
                            "brands": [
                                {
                                    "brand": "brand",
                                    "version": "version",
                                }
                            ],
                            "mobile": True,
                            "platform": "platform",
                        },
                        "vendor": "vendor",
                        "vendor_sub": "vendorSub",
                        "webdriver": True,
                    },
                    "plugins_data": {
                        "mime_types": ["string"],
                        "plugins": [
                            {
                                "description": "description",
                                "filename": "filename",
                                "mime_types": [
                                    {
                                        "description": "description",
                                        "enabled_plugin": "enabledPlugin",
                                        "suffixes": "suffixes",
                                        "type": "type",
                                    }
                                ],
                                "name": "name",
                            }
                        ],
                    },
                    "screen": {
                        "avail_height": 0,
                        "avail_left": 0,
                        "avail_top": 0,
                        "avail_width": 0,
                        "client_height": 0,
                        "client_width": 0,
                        "color_depth": 0,
                        "device_pixel_ratio": 0,
                        "has_hdr": True,
                        "height": 0,
                        "inner_height": 0,
                        "inner_width": 0,
                        "outer_height": 0,
                        "outer_width": 0,
                        "page_x_offset": 0,
                        "page_y_offset": 0,
                        "pixel_depth": 0,
                        "screen_x": 0,
                        "width": 0,
                    },
                    "slim": True,
                    "video_card": {
                        "renderer": "renderer",
                        "vendor": "vendor",
                    },
                    "video_codecs": {"foo": "string"},
                },
                "headers": {"user_agent": "user-agent"},
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Steel) -> None:
        profile = client.profiles.create(
            fingerprint={
                "fingerprint": {
                    "audio_codecs": {"foo": "string"},
                    "battery": {
                        "charging": True,
                        "charging_time": 0,
                        "discharging_time": 0,
                        "level": 0,
                    },
                    "fonts": ["string"],
                    "mock_web_rtc": True,
                    "multimedia_devices": {
                        "micros": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "speakers": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "webcams": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                    },
                    "navigator": {
                        "app_code_name": "appCodeName",
                        "app_name": "appName",
                        "app_version": "appVersion",
                        "device_memory": 0,
                        "extra_properties": {
                            "global_privacy_control": True,
                            "installed_apps": ["string"],
                            "pdf_viewer_enabled": True,
                            "vendor_flavors": ["string"],
                        },
                        "hardware_concurrency": 0,
                        "language": "language",
                        "languages": ["string"],
                        "max_touch_points": 0,
                        "oscpu": "oscpu",
                        "platform": "platform",
                        "product": "product",
                        "product_sub": "productSub",
                        "user_agent": "userAgent",
                        "user_agent_data": {
                            "brands": [
                                {
                                    "brand": "brand",
                                    "version": "version",
                                }
                            ],
                            "mobile": True,
                            "platform": "platform",
                        },
                        "vendor": "vendor",
                        "vendor_sub": "vendorSub",
                        "webdriver": True,
                        "do_not_track": "doNotTrack",
                    },
                    "plugins_data": {
                        "mime_types": ["string"],
                        "plugins": [
                            {
                                "description": "description",
                                "filename": "filename",
                                "mime_types": [
                                    {
                                        "description": "description",
                                        "enabled_plugin": "enabledPlugin",
                                        "suffixes": "suffixes",
                                        "type": "type",
                                    }
                                ],
                                "name": "name",
                            }
                        ],
                    },
                    "screen": {
                        "avail_height": 0,
                        "avail_left": 0,
                        "avail_top": 0,
                        "avail_width": 0,
                        "client_height": 0,
                        "client_width": 0,
                        "color_depth": 0,
                        "device_pixel_ratio": 0,
                        "has_hdr": True,
                        "height": 0,
                        "inner_height": 0,
                        "inner_width": 0,
                        "outer_height": 0,
                        "outer_width": 0,
                        "page_x_offset": 0,
                        "page_y_offset": 0,
                        "pixel_depth": 0,
                        "screen_x": 0,
                        "width": 0,
                    },
                    "slim": True,
                    "video_card": {
                        "renderer": "renderer",
                        "vendor": "vendor",
                    },
                    "video_codecs": {"foo": "string"},
                },
                "headers": {
                    "user_agent": "user-agent",
                    "accept": "accept",
                    "accept_encoding": "accept-encoding",
                    "accept_language": "accept-language",
                    "dnt": "dnt",
                    "sec_ch_ua": "sec-ch-ua",
                    "sec_ch_ua_mobile": "sec-ch-ua-mobile",
                    "sec_ch_ua_platform": "sec-ch-ua-platform",
                    "sec_fetch_dest": "sec-fetch-dest",
                    "sec_fetch_mode": "sec-fetch-mode",
                    "sec_fetch_site": "sec-fetch-site",
                    "sec_fetch_user": "sec-fetch-user",
                    "upgrade_insecure_requests": "upgrade-insecure-requests",
                },
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
            dimensions={
                "height": 0,
                "width": 0,
            },
            user_data_dir={},
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Steel) -> None:
        response = client.profiles.with_raw_response.create(
            fingerprint={
                "fingerprint": {
                    "audio_codecs": {"foo": "string"},
                    "battery": {
                        "charging": True,
                        "charging_time": 0,
                        "discharging_time": 0,
                        "level": 0,
                    },
                    "fonts": ["string"],
                    "mock_web_rtc": True,
                    "multimedia_devices": {
                        "micros": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "speakers": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "webcams": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                    },
                    "navigator": {
                        "app_code_name": "appCodeName",
                        "app_name": "appName",
                        "app_version": "appVersion",
                        "device_memory": 0,
                        "extra_properties": {
                            "global_privacy_control": True,
                            "installed_apps": ["string"],
                            "pdf_viewer_enabled": True,
                            "vendor_flavors": ["string"],
                        },
                        "hardware_concurrency": 0,
                        "language": "language",
                        "languages": ["string"],
                        "max_touch_points": 0,
                        "oscpu": "oscpu",
                        "platform": "platform",
                        "product": "product",
                        "product_sub": "productSub",
                        "user_agent": "userAgent",
                        "user_agent_data": {
                            "brands": [
                                {
                                    "brand": "brand",
                                    "version": "version",
                                }
                            ],
                            "mobile": True,
                            "platform": "platform",
                        },
                        "vendor": "vendor",
                        "vendor_sub": "vendorSub",
                        "webdriver": True,
                    },
                    "plugins_data": {
                        "mime_types": ["string"],
                        "plugins": [
                            {
                                "description": "description",
                                "filename": "filename",
                                "mime_types": [
                                    {
                                        "description": "description",
                                        "enabled_plugin": "enabledPlugin",
                                        "suffixes": "suffixes",
                                        "type": "type",
                                    }
                                ],
                                "name": "name",
                            }
                        ],
                    },
                    "screen": {
                        "avail_height": 0,
                        "avail_left": 0,
                        "avail_top": 0,
                        "avail_width": 0,
                        "client_height": 0,
                        "client_width": 0,
                        "color_depth": 0,
                        "device_pixel_ratio": 0,
                        "has_hdr": True,
                        "height": 0,
                        "inner_height": 0,
                        "inner_width": 0,
                        "outer_height": 0,
                        "outer_width": 0,
                        "page_x_offset": 0,
                        "page_y_offset": 0,
                        "pixel_depth": 0,
                        "screen_x": 0,
                        "width": 0,
                    },
                    "slim": True,
                    "video_card": {
                        "renderer": "renderer",
                        "vendor": "vendor",
                    },
                    "video_codecs": {"foo": "string"},
                },
                "headers": {"user_agent": "user-agent"},
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Steel) -> None:
        with client.profiles.with_streaming_response.create(
            fingerprint={
                "fingerprint": {
                    "audio_codecs": {"foo": "string"},
                    "battery": {
                        "charging": True,
                        "charging_time": 0,
                        "discharging_time": 0,
                        "level": 0,
                    },
                    "fonts": ["string"],
                    "mock_web_rtc": True,
                    "multimedia_devices": {
                        "micros": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "speakers": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "webcams": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                    },
                    "navigator": {
                        "app_code_name": "appCodeName",
                        "app_name": "appName",
                        "app_version": "appVersion",
                        "device_memory": 0,
                        "extra_properties": {
                            "global_privacy_control": True,
                            "installed_apps": ["string"],
                            "pdf_viewer_enabled": True,
                            "vendor_flavors": ["string"],
                        },
                        "hardware_concurrency": 0,
                        "language": "language",
                        "languages": ["string"],
                        "max_touch_points": 0,
                        "oscpu": "oscpu",
                        "platform": "platform",
                        "product": "product",
                        "product_sub": "productSub",
                        "user_agent": "userAgent",
                        "user_agent_data": {
                            "brands": [
                                {
                                    "brand": "brand",
                                    "version": "version",
                                }
                            ],
                            "mobile": True,
                            "platform": "platform",
                        },
                        "vendor": "vendor",
                        "vendor_sub": "vendorSub",
                        "webdriver": True,
                    },
                    "plugins_data": {
                        "mime_types": ["string"],
                        "plugins": [
                            {
                                "description": "description",
                                "filename": "filename",
                                "mime_types": [
                                    {
                                        "description": "description",
                                        "enabled_plugin": "enabledPlugin",
                                        "suffixes": "suffixes",
                                        "type": "type",
                                    }
                                ],
                                "name": "name",
                            }
                        ],
                    },
                    "screen": {
                        "avail_height": 0,
                        "avail_left": 0,
                        "avail_top": 0,
                        "avail_width": 0,
                        "client_height": 0,
                        "client_width": 0,
                        "color_depth": 0,
                        "device_pixel_ratio": 0,
                        "has_hdr": True,
                        "height": 0,
                        "inner_height": 0,
                        "inner_width": 0,
                        "outer_height": 0,
                        "outer_width": 0,
                        "page_x_offset": 0,
                        "page_y_offset": 0,
                        "pixel_depth": 0,
                        "screen_x": 0,
                        "width": 0,
                    },
                    "slim": True,
                    "video_card": {
                        "renderer": "renderer",
                        "vendor": "vendor",
                    },
                    "video_codecs": {"foo": "string"},
                },
                "headers": {"user_agent": "user-agent"},
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Steel) -> None:
        profile = client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Steel) -> None:
        response = client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Steel) -> None:
        with client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSteel) -> None:
        profile = await async_client.profiles.create(
            fingerprint={
                "fingerprint": {
                    "audio_codecs": {"foo": "string"},
                    "battery": {
                        "charging": True,
                        "charging_time": 0,
                        "discharging_time": 0,
                        "level": 0,
                    },
                    "fonts": ["string"],
                    "mock_web_rtc": True,
                    "multimedia_devices": {
                        "micros": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "speakers": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "webcams": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                    },
                    "navigator": {
                        "app_code_name": "appCodeName",
                        "app_name": "appName",
                        "app_version": "appVersion",
                        "device_memory": 0,
                        "extra_properties": {
                            "global_privacy_control": True,
                            "installed_apps": ["string"],
                            "pdf_viewer_enabled": True,
                            "vendor_flavors": ["string"],
                        },
                        "hardware_concurrency": 0,
                        "language": "language",
                        "languages": ["string"],
                        "max_touch_points": 0,
                        "oscpu": "oscpu",
                        "platform": "platform",
                        "product": "product",
                        "product_sub": "productSub",
                        "user_agent": "userAgent",
                        "user_agent_data": {
                            "brands": [
                                {
                                    "brand": "brand",
                                    "version": "version",
                                }
                            ],
                            "mobile": True,
                            "platform": "platform",
                        },
                        "vendor": "vendor",
                        "vendor_sub": "vendorSub",
                        "webdriver": True,
                    },
                    "plugins_data": {
                        "mime_types": ["string"],
                        "plugins": [
                            {
                                "description": "description",
                                "filename": "filename",
                                "mime_types": [
                                    {
                                        "description": "description",
                                        "enabled_plugin": "enabledPlugin",
                                        "suffixes": "suffixes",
                                        "type": "type",
                                    }
                                ],
                                "name": "name",
                            }
                        ],
                    },
                    "screen": {
                        "avail_height": 0,
                        "avail_left": 0,
                        "avail_top": 0,
                        "avail_width": 0,
                        "client_height": 0,
                        "client_width": 0,
                        "color_depth": 0,
                        "device_pixel_ratio": 0,
                        "has_hdr": True,
                        "height": 0,
                        "inner_height": 0,
                        "inner_width": 0,
                        "outer_height": 0,
                        "outer_width": 0,
                        "page_x_offset": 0,
                        "page_y_offset": 0,
                        "pixel_depth": 0,
                        "screen_x": 0,
                        "width": 0,
                    },
                    "slim": True,
                    "video_card": {
                        "renderer": "renderer",
                        "vendor": "vendor",
                    },
                    "video_codecs": {"foo": "string"},
                },
                "headers": {"user_agent": "user-agent"},
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSteel) -> None:
        profile = await async_client.profiles.create(
            fingerprint={
                "fingerprint": {
                    "audio_codecs": {"foo": "string"},
                    "battery": {
                        "charging": True,
                        "charging_time": 0,
                        "discharging_time": 0,
                        "level": 0,
                    },
                    "fonts": ["string"],
                    "mock_web_rtc": True,
                    "multimedia_devices": {
                        "micros": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "speakers": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "webcams": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                    },
                    "navigator": {
                        "app_code_name": "appCodeName",
                        "app_name": "appName",
                        "app_version": "appVersion",
                        "device_memory": 0,
                        "extra_properties": {
                            "global_privacy_control": True,
                            "installed_apps": ["string"],
                            "pdf_viewer_enabled": True,
                            "vendor_flavors": ["string"],
                        },
                        "hardware_concurrency": 0,
                        "language": "language",
                        "languages": ["string"],
                        "max_touch_points": 0,
                        "oscpu": "oscpu",
                        "platform": "platform",
                        "product": "product",
                        "product_sub": "productSub",
                        "user_agent": "userAgent",
                        "user_agent_data": {
                            "brands": [
                                {
                                    "brand": "brand",
                                    "version": "version",
                                }
                            ],
                            "mobile": True,
                            "platform": "platform",
                        },
                        "vendor": "vendor",
                        "vendor_sub": "vendorSub",
                        "webdriver": True,
                        "do_not_track": "doNotTrack",
                    },
                    "plugins_data": {
                        "mime_types": ["string"],
                        "plugins": [
                            {
                                "description": "description",
                                "filename": "filename",
                                "mime_types": [
                                    {
                                        "description": "description",
                                        "enabled_plugin": "enabledPlugin",
                                        "suffixes": "suffixes",
                                        "type": "type",
                                    }
                                ],
                                "name": "name",
                            }
                        ],
                    },
                    "screen": {
                        "avail_height": 0,
                        "avail_left": 0,
                        "avail_top": 0,
                        "avail_width": 0,
                        "client_height": 0,
                        "client_width": 0,
                        "color_depth": 0,
                        "device_pixel_ratio": 0,
                        "has_hdr": True,
                        "height": 0,
                        "inner_height": 0,
                        "inner_width": 0,
                        "outer_height": 0,
                        "outer_width": 0,
                        "page_x_offset": 0,
                        "page_y_offset": 0,
                        "pixel_depth": 0,
                        "screen_x": 0,
                        "width": 0,
                    },
                    "slim": True,
                    "video_card": {
                        "renderer": "renderer",
                        "vendor": "vendor",
                    },
                    "video_codecs": {"foo": "string"},
                },
                "headers": {
                    "user_agent": "user-agent",
                    "accept": "accept",
                    "accept_encoding": "accept-encoding",
                    "accept_language": "accept-language",
                    "dnt": "dnt",
                    "sec_ch_ua": "sec-ch-ua",
                    "sec_ch_ua_mobile": "sec-ch-ua-mobile",
                    "sec_ch_ua_platform": "sec-ch-ua-platform",
                    "sec_fetch_dest": "sec-fetch-dest",
                    "sec_fetch_mode": "sec-fetch-mode",
                    "sec_fetch_site": "sec-fetch-site",
                    "sec_fetch_user": "sec-fetch-user",
                    "upgrade_insecure_requests": "upgrade-insecure-requests",
                },
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
            dimensions={
                "height": 0,
                "width": 0,
            },
            user_data_dir={},
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSteel) -> None:
        response = await async_client.profiles.with_raw_response.create(
            fingerprint={
                "fingerprint": {
                    "audio_codecs": {"foo": "string"},
                    "battery": {
                        "charging": True,
                        "charging_time": 0,
                        "discharging_time": 0,
                        "level": 0,
                    },
                    "fonts": ["string"],
                    "mock_web_rtc": True,
                    "multimedia_devices": {
                        "micros": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "speakers": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "webcams": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                    },
                    "navigator": {
                        "app_code_name": "appCodeName",
                        "app_name": "appName",
                        "app_version": "appVersion",
                        "device_memory": 0,
                        "extra_properties": {
                            "global_privacy_control": True,
                            "installed_apps": ["string"],
                            "pdf_viewer_enabled": True,
                            "vendor_flavors": ["string"],
                        },
                        "hardware_concurrency": 0,
                        "language": "language",
                        "languages": ["string"],
                        "max_touch_points": 0,
                        "oscpu": "oscpu",
                        "platform": "platform",
                        "product": "product",
                        "product_sub": "productSub",
                        "user_agent": "userAgent",
                        "user_agent_data": {
                            "brands": [
                                {
                                    "brand": "brand",
                                    "version": "version",
                                }
                            ],
                            "mobile": True,
                            "platform": "platform",
                        },
                        "vendor": "vendor",
                        "vendor_sub": "vendorSub",
                        "webdriver": True,
                    },
                    "plugins_data": {
                        "mime_types": ["string"],
                        "plugins": [
                            {
                                "description": "description",
                                "filename": "filename",
                                "mime_types": [
                                    {
                                        "description": "description",
                                        "enabled_plugin": "enabledPlugin",
                                        "suffixes": "suffixes",
                                        "type": "type",
                                    }
                                ],
                                "name": "name",
                            }
                        ],
                    },
                    "screen": {
                        "avail_height": 0,
                        "avail_left": 0,
                        "avail_top": 0,
                        "avail_width": 0,
                        "client_height": 0,
                        "client_width": 0,
                        "color_depth": 0,
                        "device_pixel_ratio": 0,
                        "has_hdr": True,
                        "height": 0,
                        "inner_height": 0,
                        "inner_width": 0,
                        "outer_height": 0,
                        "outer_width": 0,
                        "page_x_offset": 0,
                        "page_y_offset": 0,
                        "pixel_depth": 0,
                        "screen_x": 0,
                        "width": 0,
                    },
                    "slim": True,
                    "video_card": {
                        "renderer": "renderer",
                        "vendor": "vendor",
                    },
                    "video_codecs": {"foo": "string"},
                },
                "headers": {"user_agent": "user-agent"},
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSteel) -> None:
        async with async_client.profiles.with_streaming_response.create(
            fingerprint={
                "fingerprint": {
                    "audio_codecs": {"foo": "string"},
                    "battery": {
                        "charging": True,
                        "charging_time": 0,
                        "discharging_time": 0,
                        "level": 0,
                    },
                    "fonts": ["string"],
                    "mock_web_rtc": True,
                    "multimedia_devices": {
                        "micros": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "speakers": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                        "webcams": [
                            {
                                "device_id": "deviceId",
                                "group_id": "groupId",
                                "kind": "kind",
                                "label": "label",
                            }
                        ],
                    },
                    "navigator": {
                        "app_code_name": "appCodeName",
                        "app_name": "appName",
                        "app_version": "appVersion",
                        "device_memory": 0,
                        "extra_properties": {
                            "global_privacy_control": True,
                            "installed_apps": ["string"],
                            "pdf_viewer_enabled": True,
                            "vendor_flavors": ["string"],
                        },
                        "hardware_concurrency": 0,
                        "language": "language",
                        "languages": ["string"],
                        "max_touch_points": 0,
                        "oscpu": "oscpu",
                        "platform": "platform",
                        "product": "product",
                        "product_sub": "productSub",
                        "user_agent": "userAgent",
                        "user_agent_data": {
                            "brands": [
                                {
                                    "brand": "brand",
                                    "version": "version",
                                }
                            ],
                            "mobile": True,
                            "platform": "platform",
                        },
                        "vendor": "vendor",
                        "vendor_sub": "vendorSub",
                        "webdriver": True,
                    },
                    "plugins_data": {
                        "mime_types": ["string"],
                        "plugins": [
                            {
                                "description": "description",
                                "filename": "filename",
                                "mime_types": [
                                    {
                                        "description": "description",
                                        "enabled_plugin": "enabledPlugin",
                                        "suffixes": "suffixes",
                                        "type": "type",
                                    }
                                ],
                                "name": "name",
                            }
                        ],
                    },
                    "screen": {
                        "avail_height": 0,
                        "avail_left": 0,
                        "avail_top": 0,
                        "avail_width": 0,
                        "client_height": 0,
                        "client_width": 0,
                        "color_depth": 0,
                        "device_pixel_ratio": 0,
                        "has_hdr": True,
                        "height": 0,
                        "inner_height": 0,
                        "inner_width": 0,
                        "outer_height": 0,
                        "outer_width": 0,
                        "page_x_offset": 0,
                        "page_y_offset": 0,
                        "pixel_depth": 0,
                        "screen_x": 0,
                        "width": 0,
                    },
                    "slim": True,
                    "video_card": {
                        "renderer": "renderer",
                        "vendor": "vendor",
                    },
                    "video_codecs": {"foo": "string"},
                },
                "headers": {"user_agent": "user-agent"},
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSteel) -> None:
        profile = await async_client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSteel) -> None:
        response = await async_client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSteel) -> None:
        async with async_client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
