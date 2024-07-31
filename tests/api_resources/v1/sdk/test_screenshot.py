# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScreenshot:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Steel) -> None:
        screenshot = client.v1.sdk.screenshot.create(
            url="https://example.com",
        )
        assert_matches_type(object, screenshot, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Steel) -> None:
        response = client.v1.sdk.screenshot.with_raw_response.create(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = response.parse()
        assert_matches_type(object, screenshot, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Steel) -> None:
        with client.v1.sdk.screenshot.with_streaming_response.create(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = response.parse()
            assert_matches_type(object, screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScreenshot:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSteel) -> None:
        screenshot = await async_client.v1.sdk.screenshot.create(
            url="https://example.com",
        )
        assert_matches_type(object, screenshot, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSteel) -> None:
        response = await async_client.v1.sdk.screenshot.with_raw_response.create(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = await response.parse()
        assert_matches_type(object, screenshot, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSteel) -> None:
        async with async_client.v1.sdk.screenshot.with_streaming_response.create(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = await response.parse()
            assert_matches_type(object, screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True
