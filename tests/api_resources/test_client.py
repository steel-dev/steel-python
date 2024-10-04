# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import (
    PdfResponse,
    ScrapeResponse,
    ScreenshotResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopLevel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_pdf(self, client: Steel) -> None:
        top_level = client.pdf(
            url="url",
        )
        assert_matches_type(PdfResponse, top_level, path=["response"])

    @parametrize
    def test_method_pdf_with_all_params(self, client: Steel) -> None:
        top_level = client.pdf(
            url="url",
            use_proxy=True,
        )
        assert_matches_type(PdfResponse, top_level, path=["response"])

    @parametrize
    def test_raw_response_pdf(self, client: Steel) -> None:
        response = client.with_raw_response.pdf(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(PdfResponse, top_level, path=["response"])

    @parametrize
    def test_streaming_response_pdf(self, client: Steel) -> None:
        with client.with_streaming_response.pdf(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = response.parse()
            assert_matches_type(PdfResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_scrape(self, client: Steel) -> None:
        top_level = client.scrape(
            url="url",
        )
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    def test_method_scrape_with_all_params(self, client: Steel) -> None:
        top_level = client.scrape(
            url="url",
            delay=0,
            format=["html", "readability", "cleaned_html"],
            pdf=True,
            screenshot=True,
            use_proxy=True,
        )
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    def test_raw_response_scrape(self, client: Steel) -> None:
        response = client.with_raw_response.scrape(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    def test_streaming_response_scrape(self, client: Steel) -> None:
        with client.with_streaming_response.scrape(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = response.parse()
            assert_matches_type(ScrapeResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_screenshot(self, client: Steel) -> None:
        top_level = client.screenshot(
            url="url",
        )
        assert_matches_type(ScreenshotResponse, top_level, path=["response"])

    @parametrize
    def test_method_screenshot_with_all_params(self, client: Steel) -> None:
        top_level = client.screenshot(
            url="url",
            use_proxy=True,
        )
        assert_matches_type(ScreenshotResponse, top_level, path=["response"])

    @parametrize
    def test_raw_response_screenshot(self, client: Steel) -> None:
        response = client.with_raw_response.screenshot(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(ScreenshotResponse, top_level, path=["response"])

    @parametrize
    def test_streaming_response_screenshot(self, client: Steel) -> None:
        with client.with_streaming_response.screenshot(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = response.parse()
            assert_matches_type(ScreenshotResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTopLevel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_pdf(self, async_client: AsyncSteel) -> None:
        top_level = await async_client.pdf(
            url="url",
        )
        assert_matches_type(PdfResponse, top_level, path=["response"])

    @parametrize
    async def test_method_pdf_with_all_params(self, async_client: AsyncSteel) -> None:
        top_level = await async_client.pdf(
            url="url",
            use_proxy=True,
        )
        assert_matches_type(PdfResponse, top_level, path=["response"])

    @parametrize
    async def test_raw_response_pdf(self, async_client: AsyncSteel) -> None:
        response = await async_client.with_raw_response.pdf(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = await response.parse()
        assert_matches_type(PdfResponse, top_level, path=["response"])

    @parametrize
    async def test_streaming_response_pdf(self, async_client: AsyncSteel) -> None:
        async with async_client.with_streaming_response.pdf(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = await response.parse()
            assert_matches_type(PdfResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_scrape(self, async_client: AsyncSteel) -> None:
        top_level = await async_client.scrape(
            url="url",
        )
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    async def test_method_scrape_with_all_params(self, async_client: AsyncSteel) -> None:
        top_level = await async_client.scrape(
            url="url",
            delay=0,
            format=["html", "readability", "cleaned_html"],
            pdf=True,
            screenshot=True,
            use_proxy=True,
        )
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    async def test_raw_response_scrape(self, async_client: AsyncSteel) -> None:
        response = await async_client.with_raw_response.scrape(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = await response.parse()
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    async def test_streaming_response_scrape(self, async_client: AsyncSteel) -> None:
        async with async_client.with_streaming_response.scrape(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = await response.parse()
            assert_matches_type(ScrapeResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_screenshot(self, async_client: AsyncSteel) -> None:
        top_level = await async_client.screenshot(
            url="url",
        )
        assert_matches_type(ScreenshotResponse, top_level, path=["response"])

    @parametrize
    async def test_method_screenshot_with_all_params(self, async_client: AsyncSteel) -> None:
        top_level = await async_client.screenshot(
            url="url",
            use_proxy=True,
        )
        assert_matches_type(ScreenshotResponse, top_level, path=["response"])

    @parametrize
    async def test_raw_response_screenshot(self, async_client: AsyncSteel) -> None:
        response = await async_client.with_raw_response.screenshot(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = await response.parse()
        assert_matches_type(ScreenshotResponse, top_level, path=["response"])

    @parametrize
    async def test_streaming_response_screenshot(self, async_client: AsyncSteel) -> None:
        async with async_client.with_streaming_response.screenshot(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = await response.parse()
            assert_matches_type(ScreenshotResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True
