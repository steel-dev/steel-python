# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from steel import Steel, AsyncSteel
from steel.types import Scrape
from tests.utils import assert_matches_type
from steel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowserTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_pdf(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        browser_tool = client.browser_tools.pdf(
            url="url",
        )
        assert browser_tool.is_closed
        assert browser_tool.json() == {"foo": "bar"}
        assert cast(Any, browser_tool.is_closed) is True
        assert isinstance(browser_tool, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_pdf(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        browser_tool = client.browser_tools.with_raw_response.pdf(
            url="url",
        )

        assert browser_tool.is_closed is True
        assert browser_tool.http_request.headers.get("X-Stainless-Lang") == "python"
        assert browser_tool.json() == {"foo": "bar"}
        assert isinstance(browser_tool, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_pdf(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.browser_tools.with_streaming_response.pdf(
            url="url",
        ) as browser_tool:
            assert not browser_tool.is_closed
            assert browser_tool.http_request.headers.get("X-Stainless-Lang") == "python"

            assert browser_tool.json() == {"foo": "bar"}
            assert cast(Any, browser_tool.is_closed) is True
            assert isinstance(browser_tool, StreamedBinaryAPIResponse)

        assert cast(Any, browser_tool.is_closed) is True

    @parametrize
    def test_method_scrape(self, client: Steel) -> None:
        browser_tool = client.browser_tools.scrape(
            url="url",
        )
        assert_matches_type(Scrape, browser_tool, path=["response"])

    @parametrize
    def test_method_scrape_with_all_params(self, client: Steel) -> None:
        browser_tool = client.browser_tools.scrape(
            url="url",
            format=["html", "cleaned_html", "readability"],
            screenshot=True,
        )
        assert_matches_type(Scrape, browser_tool, path=["response"])

    @parametrize
    def test_raw_response_scrape(self, client: Steel) -> None:
        response = client.browser_tools.with_raw_response.scrape(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_tool = response.parse()
        assert_matches_type(Scrape, browser_tool, path=["response"])

    @parametrize
    def test_streaming_response_scrape(self, client: Steel) -> None:
        with client.browser_tools.with_streaming_response.scrape(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_tool = response.parse()
            assert_matches_type(Scrape, browser_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_screenshot(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        browser_tool = client.browser_tools.screenshot(
            url="url",
        )
        assert browser_tool.is_closed
        assert browser_tool.json() == {"foo": "bar"}
        assert cast(Any, browser_tool.is_closed) is True
        assert isinstance(browser_tool, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_screenshot(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        browser_tool = client.browser_tools.with_raw_response.screenshot(
            url="url",
        )

        assert browser_tool.is_closed is True
        assert browser_tool.http_request.headers.get("X-Stainless-Lang") == "python"
        assert browser_tool.json() == {"foo": "bar"}
        assert isinstance(browser_tool, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_screenshot(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.browser_tools.with_streaming_response.screenshot(
            url="url",
        ) as browser_tool:
            assert not browser_tool.is_closed
            assert browser_tool.http_request.headers.get("X-Stainless-Lang") == "python"

            assert browser_tool.json() == {"foo": "bar"}
            assert cast(Any, browser_tool.is_closed) is True
            assert isinstance(browser_tool, StreamedBinaryAPIResponse)

        assert cast(Any, browser_tool.is_closed) is True


class TestAsyncBrowserTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_pdf(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        browser_tool = await async_client.browser_tools.pdf(
            url="url",
        )
        assert browser_tool.is_closed
        assert await browser_tool.json() == {"foo": "bar"}
        assert cast(Any, browser_tool.is_closed) is True
        assert isinstance(browser_tool, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_pdf(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        browser_tool = await async_client.browser_tools.with_raw_response.pdf(
            url="url",
        )

        assert browser_tool.is_closed is True
        assert browser_tool.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await browser_tool.json() == {"foo": "bar"}
        assert isinstance(browser_tool, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_pdf(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.browser_tools.with_streaming_response.pdf(
            url="url",
        ) as browser_tool:
            assert not browser_tool.is_closed
            assert browser_tool.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await browser_tool.json() == {"foo": "bar"}
            assert cast(Any, browser_tool.is_closed) is True
            assert isinstance(browser_tool, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, browser_tool.is_closed) is True

    @parametrize
    async def test_method_scrape(self, async_client: AsyncSteel) -> None:
        browser_tool = await async_client.browser_tools.scrape(
            url="url",
        )
        assert_matches_type(Scrape, browser_tool, path=["response"])

    @parametrize
    async def test_method_scrape_with_all_params(self, async_client: AsyncSteel) -> None:
        browser_tool = await async_client.browser_tools.scrape(
            url="url",
            format=["html", "cleaned_html", "readability"],
            screenshot=True,
        )
        assert_matches_type(Scrape, browser_tool, path=["response"])

    @parametrize
    async def test_raw_response_scrape(self, async_client: AsyncSteel) -> None:
        response = await async_client.browser_tools.with_raw_response.scrape(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_tool = await response.parse()
        assert_matches_type(Scrape, browser_tool, path=["response"])

    @parametrize
    async def test_streaming_response_scrape(self, async_client: AsyncSteel) -> None:
        async with async_client.browser_tools.with_streaming_response.scrape(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_tool = await response.parse()
            assert_matches_type(Scrape, browser_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_screenshot(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        browser_tool = await async_client.browser_tools.screenshot(
            url="url",
        )
        assert browser_tool.is_closed
        assert await browser_tool.json() == {"foo": "bar"}
        assert cast(Any, browser_tool.is_closed) is True
        assert isinstance(browser_tool, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_screenshot(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        browser_tool = await async_client.browser_tools.with_raw_response.screenshot(
            url="url",
        )

        assert browser_tool.is_closed is True
        assert browser_tool.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await browser_tool.json() == {"foo": "bar"}
        assert isinstance(browser_tool, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_screenshot(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.browser_tools.with_streaming_response.screenshot(
            url="url",
        ) as browser_tool:
            assert not browser_tool.is_closed
            assert browser_tool.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await browser_tool.json() == {"foo": "bar"}
            assert cast(Any, browser_tool.is_closed) is True
            assert isinstance(browser_tool, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, browser_tool.is_closed) is True
