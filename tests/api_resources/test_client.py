# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from steel import Steel, AsyncSteel
from steel.types import ScrapeResponse
from tests.utils import assert_matches_type
from steel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopLevel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_pdf(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        top_level = client.pdf(
            url="url",
        )
        assert top_level.is_closed
        assert top_level.json() == {"foo": "bar"}
        assert cast(Any, top_level.is_closed) is True
        assert isinstance(top_level, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_pdf(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        top_level = client.with_raw_response.pdf(
            url="url",
        )

        assert top_level.is_closed is True
        assert top_level.http_request.headers.get("X-Stainless-Lang") == "python"
        assert top_level.json() == {"foo": "bar"}
        assert isinstance(top_level, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_pdf(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.with_streaming_response.pdf(
            url="url",
        ) as top_level:
            assert not top_level.is_closed
            assert top_level.http_request.headers.get("X-Stainless-Lang") == "python"

            assert top_level.json() == {"foo": "bar"}
            assert cast(Any, top_level.is_closed) is True
            assert isinstance(top_level, StreamedBinaryAPIResponse)

        assert cast(Any, top_level.is_closed) is True

    @parametrize
    def test_method_scrape(self, client: Steel) -> None:
        top_level = client.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    def test_method_scrape_with_all_params(self, client: Steel) -> None:
        top_level = client.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            format=["html", "cleaned_html", "readability"],
        )
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    def test_raw_response_scrape(self, client: Steel) -> None:
        response = client.with_raw_response.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    def test_streaming_response_scrape(self, client: Steel) -> None:
        with client.with_streaming_response.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = response.parse()
            assert_matches_type(ScrapeResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_screenshot(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        top_level = client.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert top_level.is_closed
        assert top_level.json() == {"foo": "bar"}
        assert cast(Any, top_level.is_closed) is True
        assert isinstance(top_level, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_screenshot(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        top_level = client.with_raw_response.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert top_level.is_closed is True
        assert top_level.http_request.headers.get("X-Stainless-Lang") == "python"
        assert top_level.json() == {"foo": "bar"}
        assert isinstance(top_level, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_screenshot(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.with_streaming_response.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as top_level:
            assert not top_level.is_closed
            assert top_level.http_request.headers.get("X-Stainless-Lang") == "python"

            assert top_level.json() == {"foo": "bar"}
            assert cast(Any, top_level.is_closed) is True
            assert isinstance(top_level, StreamedBinaryAPIResponse)

        assert cast(Any, top_level.is_closed) is True


class TestAsyncTopLevel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_pdf(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        top_level = await async_client.pdf(
            url="url",
        )
        assert top_level.is_closed
        assert await top_level.json() == {"foo": "bar"}
        assert cast(Any, top_level.is_closed) is True
        assert isinstance(top_level, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_pdf(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        top_level = await async_client.with_raw_response.pdf(
            url="url",
        )

        assert top_level.is_closed is True
        assert top_level.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await top_level.json() == {"foo": "bar"}
        assert isinstance(top_level, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_pdf(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.with_streaming_response.pdf(
            url="url",
        ) as top_level:
            assert not top_level.is_closed
            assert top_level.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await top_level.json() == {"foo": "bar"}
            assert cast(Any, top_level.is_closed) is True
            assert isinstance(top_level, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, top_level.is_closed) is True

    @parametrize
    async def test_method_scrape(self, async_client: AsyncSteel) -> None:
        top_level = await async_client.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    async def test_method_scrape_with_all_params(self, async_client: AsyncSteel) -> None:
        top_level = await async_client.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            format=["html", "cleaned_html", "readability"],
        )
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    async def test_raw_response_scrape(self, async_client: AsyncSteel) -> None:
        response = await async_client.with_raw_response.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = await response.parse()
        assert_matches_type(ScrapeResponse, top_level, path=["response"])

    @parametrize
    async def test_streaming_response_scrape(self, async_client: AsyncSteel) -> None:
        async with async_client.with_streaming_response.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = await response.parse()
            assert_matches_type(ScrapeResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_screenshot(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        top_level = await async_client.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert top_level.is_closed
        assert await top_level.json() == {"foo": "bar"}
        assert cast(Any, top_level.is_closed) is True
        assert isinstance(top_level, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_screenshot(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        top_level = await async_client.with_raw_response.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert top_level.is_closed is True
        assert top_level.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await top_level.json() == {"foo": "bar"}
        assert isinstance(top_level, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_screenshot(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.with_streaming_response.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as top_level:
            assert not top_level.is_closed
            assert top_level.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await top_level.json() == {"foo": "bar"}
            assert cast(Any, top_level.is_closed) is True
            assert isinstance(top_level, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, top_level.is_closed) is True
