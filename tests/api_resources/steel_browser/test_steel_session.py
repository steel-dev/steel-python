# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from tests.utils import assert_matches_type
from steel.types.steel_browser import Session, SteelSessionReleaseSessionResponse
from steel.types.steel_browser.steel_session import Context

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteelSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_context(self, client: Steel) -> None:
        steel_session = client.steel_browser.steel_session.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Context, steel_session, path=["response"])

    @parametrize
    def test_raw_response_get_context(self, client: Steel) -> None:
        response = client.steel_browser.steel_session.with_raw_response.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_session = response.parse()
        assert_matches_type(Context, steel_session, path=["response"])

    @parametrize
    def test_streaming_response_get_context(self, client: Steel) -> None:
        with client.steel_browser.steel_session.with_streaming_response.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_session = response.parse()
            assert_matches_type(Context, steel_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_context(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.steel_browser.steel_session.with_raw_response.get_context(
                "",
            )

    @parametrize
    def test_method_get_session_data(self, client: Steel) -> None:
        steel_session = client.steel_browser.steel_session.get_session_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, steel_session, path=["response"])

    @parametrize
    def test_raw_response_get_session_data(self, client: Steel) -> None:
        response = client.steel_browser.steel_session.with_raw_response.get_session_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_session = response.parse()
        assert_matches_type(Session, steel_session, path=["response"])

    @parametrize
    def test_streaming_response_get_session_data(self, client: Steel) -> None:
        with client.steel_browser.steel_session.with_streaming_response.get_session_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_session = response.parse()
            assert_matches_type(Session, steel_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_session_data(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.steel_browser.steel_session.with_raw_response.get_session_data(
                id="",
                orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_release_session(self, client: Steel) -> None:
        steel_session = client.steel_browser.steel_session.release_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SteelSessionReleaseSessionResponse, steel_session, path=["response"])

    @parametrize
    def test_raw_response_release_session(self, client: Steel) -> None:
        response = client.steel_browser.steel_session.with_raw_response.release_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_session = response.parse()
        assert_matches_type(SteelSessionReleaseSessionResponse, steel_session, path=["response"])

    @parametrize
    def test_streaming_response_release_session(self, client: Steel) -> None:
        with client.steel_browser.steel_session.with_streaming_response.release_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_session = response.parse()
            assert_matches_type(SteelSessionReleaseSessionResponse, steel_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_release_session(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.steel_browser.steel_session.with_raw_response.release_session(
                id="",
                orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSteelSession:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_context(self, async_client: AsyncSteel) -> None:
        steel_session = await async_client.steel_browser.steel_session.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Context, steel_session, path=["response"])

    @parametrize
    async def test_raw_response_get_context(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.steel_session.with_raw_response.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_session = await response.parse()
        assert_matches_type(Context, steel_session, path=["response"])

    @parametrize
    async def test_streaming_response_get_context(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.steel_session.with_streaming_response.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_session = await response.parse()
            assert_matches_type(Context, steel_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_context(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.steel_browser.steel_session.with_raw_response.get_context(
                "",
            )

    @parametrize
    async def test_method_get_session_data(self, async_client: AsyncSteel) -> None:
        steel_session = await async_client.steel_browser.steel_session.get_session_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, steel_session, path=["response"])

    @parametrize
    async def test_raw_response_get_session_data(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.steel_session.with_raw_response.get_session_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_session = await response.parse()
        assert_matches_type(Session, steel_session, path=["response"])

    @parametrize
    async def test_streaming_response_get_session_data(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.steel_session.with_streaming_response.get_session_data(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_session = await response.parse()
            assert_matches_type(Session, steel_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_session_data(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.steel_browser.steel_session.with_raw_response.get_session_data(
                id="",
                orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_release_session(self, async_client: AsyncSteel) -> None:
        steel_session = await async_client.steel_browser.steel_session.release_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SteelSessionReleaseSessionResponse, steel_session, path=["response"])

    @parametrize
    async def test_raw_response_release_session(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.steel_session.with_raw_response.release_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_session = await response.parse()
        assert_matches_type(SteelSessionReleaseSessionResponse, steel_session, path=["response"])

    @parametrize
    async def test_streaming_response_release_session(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.steel_session.with_streaming_response.release_session(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_session = await response.parse()
            assert_matches_type(SteelSessionReleaseSessionResponse, steel_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_release_session(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.steel_browser.steel_session.with_raw_response.release_session(
                id="",
                orgid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
