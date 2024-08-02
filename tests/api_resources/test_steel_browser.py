# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from steel import Steel, AsyncSteel
from steel.types import (
    SteelBrowserScrapeResponse,
    SteelBrowserListSessionsResponse,
)
from tests.utils import assert_matches_type
from steel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from steel.types.steel_browser import Session

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteelBrowser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_session(self, client: Steel) -> None:
        steel_browser = client.steel_browser.create_session(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    def test_method_create_session_with_all_params(self, client: Steel) -> None:
        steel_browser = client.steel_browser.create_session(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context_data={},
            proxy="proxy",
            region="CA",
            solve_captcha=True,
            user_agent="userAgent",
        )
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    def test_raw_response_create_session(self, client: Steel) -> None:
        response = client.steel_browser.with_raw_response.create_session(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_browser = response.parse()
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    def test_streaming_response_create_session(self, client: Steel) -> None:
        with client.steel_browser.with_streaming_response.create_session(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_browser = response.parse()
            assert_matches_type(Session, steel_browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_sessions(self, client: Steel) -> None:
        steel_browser = client.steel_browser.list_sessions(
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SteelBrowserListSessionsResponse, steel_browser, path=["response"])

    @parametrize
    def test_method_list_sessions_with_all_params(self, client: Steel) -> None:
        steel_browser = client.steel_browser.list_sessions(
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            live_only=True,
        )
        assert_matches_type(SteelBrowserListSessionsResponse, steel_browser, path=["response"])

    @parametrize
    def test_raw_response_list_sessions(self, client: Steel) -> None:
        response = client.steel_browser.with_raw_response.list_sessions(
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_browser = response.parse()
        assert_matches_type(SteelBrowserListSessionsResponse, steel_browser, path=["response"])

    @parametrize
    def test_streaming_response_list_sessions(self, client: Steel) -> None:
        with client.steel_browser.with_streaming_response.list_sessions(
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_browser = response.parse()
            assert_matches_type(SteelBrowserListSessionsResponse, steel_browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_pdf(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        steel_browser = client.steel_browser.pdf(
            url="url",
        )
        assert steel_browser.is_closed
        assert steel_browser.json() == {"foo": "bar"}
        assert cast(Any, steel_browser.is_closed) is True
        assert isinstance(steel_browser, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_pdf(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        steel_browser = client.steel_browser.with_raw_response.pdf(
            url="url",
        )

        assert steel_browser.is_closed is True
        assert steel_browser.http_request.headers.get("X-Stainless-Lang") == "python"
        assert steel_browser.json() == {"foo": "bar"}
        assert isinstance(steel_browser, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_pdf(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.steel_browser.with_streaming_response.pdf(
            url="url",
        ) as steel_browser:
            assert not steel_browser.is_closed
            assert steel_browser.http_request.headers.get("X-Stainless-Lang") == "python"

            assert steel_browser.json() == {"foo": "bar"}
            assert cast(Any, steel_browser.is_closed) is True
            assert isinstance(steel_browser, StreamedBinaryAPIResponse)

        assert cast(Any, steel_browser.is_closed) is True

    @parametrize
    def test_method_retrieve_session(self, client: Steel) -> None:
        steel_browser = client.steel_browser.retrieve_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    def test_raw_response_retrieve_session(self, client: Steel) -> None:
        response = client.steel_browser.with_raw_response.retrieve_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_browser = response.parse()
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_session(self, client: Steel) -> None:
        with client.steel_browser.with_streaming_response.retrieve_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_browser = response.parse()
            assert_matches_type(Session, steel_browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_session(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.steel_browser.with_raw_response.retrieve_session(
                id="",
                orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_scrape(self, client: Steel) -> None:
        steel_browser = client.steel_browser.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SteelBrowserScrapeResponse, steel_browser, path=["response"])

    @parametrize
    def test_method_scrape_with_all_params(self, client: Steel) -> None:
        steel_browser = client.steel_browser.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            format=["html", "cleaned_html", "readability"],
            screenshot=True,
        )
        assert_matches_type(SteelBrowserScrapeResponse, steel_browser, path=["response"])

    @parametrize
    def test_raw_response_scrape(self, client: Steel) -> None:
        response = client.steel_browser.with_raw_response.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_browser = response.parse()
        assert_matches_type(SteelBrowserScrapeResponse, steel_browser, path=["response"])

    @parametrize
    def test_streaming_response_scrape(self, client: Steel) -> None:
        with client.steel_browser.with_streaming_response.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_browser = response.parse()
            assert_matches_type(SteelBrowserScrapeResponse, steel_browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_screenshot(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        steel_browser = client.steel_browser.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert steel_browser.is_closed
        assert steel_browser.json() == {"foo": "bar"}
        assert cast(Any, steel_browser.is_closed) is True
        assert isinstance(steel_browser, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_screenshot(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        steel_browser = client.steel_browser.with_raw_response.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert steel_browser.is_closed is True
        assert steel_browser.http_request.headers.get("X-Stainless-Lang") == "python"
        assert steel_browser.json() == {"foo": "bar"}
        assert isinstance(steel_browser, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_screenshot(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.steel_browser.with_streaming_response.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as steel_browser:
            assert not steel_browser.is_closed
            assert steel_browser.http_request.headers.get("X-Stainless-Lang") == "python"

            assert steel_browser.json() == {"foo": "bar"}
            assert cast(Any, steel_browser.is_closed) is True
            assert isinstance(steel_browser, StreamedBinaryAPIResponse)

        assert cast(Any, steel_browser.is_closed) is True


class TestAsyncSteelBrowser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_session(self, async_client: AsyncSteel) -> None:
        steel_browser = await async_client.steel_browser.create_session(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    async def test_method_create_session_with_all_params(self, async_client: AsyncSteel) -> None:
        steel_browser = await async_client.steel_browser.create_session(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context_data={},
            proxy="proxy",
            region="CA",
            solve_captcha=True,
            user_agent="userAgent",
        )
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.with_raw_response.create_session(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_browser = await response.parse()
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.with_streaming_response.create_session(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_browser = await response.parse()
            assert_matches_type(Session, steel_browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_sessions(self, async_client: AsyncSteel) -> None:
        steel_browser = await async_client.steel_browser.list_sessions(
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SteelBrowserListSessionsResponse, steel_browser, path=["response"])

    @parametrize
    async def test_method_list_sessions_with_all_params(self, async_client: AsyncSteel) -> None:
        steel_browser = await async_client.steel_browser.list_sessions(
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            live_only=True,
        )
        assert_matches_type(SteelBrowserListSessionsResponse, steel_browser, path=["response"])

    @parametrize
    async def test_raw_response_list_sessions(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.with_raw_response.list_sessions(
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_browser = await response.parse()
        assert_matches_type(SteelBrowserListSessionsResponse, steel_browser, path=["response"])

    @parametrize
    async def test_streaming_response_list_sessions(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.with_streaming_response.list_sessions(
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_browser = await response.parse()
            assert_matches_type(SteelBrowserListSessionsResponse, steel_browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_pdf(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        steel_browser = await async_client.steel_browser.pdf(
            url="url",
        )
        assert steel_browser.is_closed
        assert await steel_browser.json() == {"foo": "bar"}
        assert cast(Any, steel_browser.is_closed) is True
        assert isinstance(steel_browser, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_pdf(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        steel_browser = await async_client.steel_browser.with_raw_response.pdf(
            url="url",
        )

        assert steel_browser.is_closed is True
        assert steel_browser.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await steel_browser.json() == {"foo": "bar"}
        assert isinstance(steel_browser, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_pdf(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/pdf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.steel_browser.with_streaming_response.pdf(
            url="url",
        ) as steel_browser:
            assert not steel_browser.is_closed
            assert steel_browser.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await steel_browser.json() == {"foo": "bar"}
            assert cast(Any, steel_browser.is_closed) is True
            assert isinstance(steel_browser, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, steel_browser.is_closed) is True

    @parametrize
    async def test_method_retrieve_session(self, async_client: AsyncSteel) -> None:
        steel_browser = await async_client.steel_browser.retrieve_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_session(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.with_raw_response.retrieve_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_browser = await response.parse()
        assert_matches_type(Session, steel_browser, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_session(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.with_streaming_response.retrieve_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_browser = await response.parse()
            assert_matches_type(Session, steel_browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_session(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.steel_browser.with_raw_response.retrieve_session(
                id="",
                orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_scrape(self, async_client: AsyncSteel) -> None:
        steel_browser = await async_client.steel_browser.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SteelBrowserScrapeResponse, steel_browser, path=["response"])

    @parametrize
    async def test_method_scrape_with_all_params(self, async_client: AsyncSteel) -> None:
        steel_browser = await async_client.steel_browser.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            format=["html", "cleaned_html", "readability"],
            screenshot=True,
        )
        assert_matches_type(SteelBrowserScrapeResponse, steel_browser, path=["response"])

    @parametrize
    async def test_raw_response_scrape(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.with_raw_response.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_browser = await response.parse()
        assert_matches_type(SteelBrowserScrapeResponse, steel_browser, path=["response"])

    @parametrize
    async def test_streaming_response_scrape(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.with_streaming_response.scrape(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_browser = await response.parse()
            assert_matches_type(SteelBrowserScrapeResponse, steel_browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_screenshot(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        steel_browser = await async_client.steel_browser.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert steel_browser.is_closed
        assert await steel_browser.json() == {"foo": "bar"}
        assert cast(Any, steel_browser.is_closed) is True
        assert isinstance(steel_browser, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_screenshot(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        steel_browser = await async_client.steel_browser.with_raw_response.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert steel_browser.is_closed is True
        assert steel_browser.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await steel_browser.json() == {"foo": "bar"}
        assert isinstance(steel_browser, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_screenshot(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/screenshot").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.steel_browser.with_streaming_response.screenshot(
            url="url",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as steel_browser:
            assert not steel_browser.is_closed
            assert steel_browser.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await steel_browser.json() == {"foo": "bar"}
            assert cast(Any, steel_browser.is_closed) is True
            assert isinstance(steel_browser, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, steel_browser.is_closed) is True
