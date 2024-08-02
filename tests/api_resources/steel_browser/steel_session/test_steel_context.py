# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from tests.utils import assert_matches_type
from steel.types.steel_browser.steel_session import (
    Context,
    SteelContextCreateContextResponse,
    SteelContextDeleteContextResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteelContext:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_context(self, client: Steel) -> None:
        steel_context = client.steel_browser.steel_session.steel_context.create_context()
        assert_matches_type(SteelContextCreateContextResponse, steel_context, path=["response"])

    @parametrize
    def test_method_create_context_with_all_params(self, client: Steel) -> None:
        steel_context = client.steel_browser.steel_session.steel_context.create_context(
            proxy="proxy",
        )
        assert_matches_type(SteelContextCreateContextResponse, steel_context, path=["response"])

    @parametrize
    def test_raw_response_create_context(self, client: Steel) -> None:
        response = client.steel_browser.steel_session.steel_context.with_raw_response.create_context()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_context = response.parse()
        assert_matches_type(SteelContextCreateContextResponse, steel_context, path=["response"])

    @parametrize
    def test_streaming_response_create_context(self, client: Steel) -> None:
        with client.steel_browser.steel_session.steel_context.with_streaming_response.create_context() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_context = response.parse()
            assert_matches_type(SteelContextCreateContextResponse, steel_context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_context(self, client: Steel) -> None:
        steel_context = client.steel_browser.steel_session.steel_context.delete_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SteelContextDeleteContextResponse, steel_context, path=["response"])

    @parametrize
    def test_raw_response_delete_context(self, client: Steel) -> None:
        response = client.steel_browser.steel_session.steel_context.with_raw_response.delete_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_context = response.parse()
        assert_matches_type(SteelContextDeleteContextResponse, steel_context, path=["response"])

    @parametrize
    def test_streaming_response_delete_context(self, client: Steel) -> None:
        with client.steel_browser.steel_session.steel_context.with_streaming_response.delete_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_context = response.parse()
            assert_matches_type(SteelContextDeleteContextResponse, steel_context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_context(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.steel_browser.steel_session.steel_context.with_raw_response.delete_context(
                "",
            )

    @parametrize
    def test_method_get_context_data(self, client: Steel) -> None:
        steel_context = client.steel_browser.steel_session.steel_context.get_context_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Context, steel_context, path=["response"])

    @parametrize
    def test_raw_response_get_context_data(self, client: Steel) -> None:
        response = client.steel_browser.steel_session.steel_context.with_raw_response.get_context_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_context = response.parse()
        assert_matches_type(Context, steel_context, path=["response"])

    @parametrize
    def test_streaming_response_get_context_data(self, client: Steel) -> None:
        with client.steel_browser.steel_session.steel_context.with_streaming_response.get_context_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_context = response.parse()
            assert_matches_type(Context, steel_context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_context_data(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.steel_browser.steel_session.steel_context.with_raw_response.get_context_data(
                "",
            )


class TestAsyncSteelContext:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_context(self, async_client: AsyncSteel) -> None:
        steel_context = await async_client.steel_browser.steel_session.steel_context.create_context()
        assert_matches_type(SteelContextCreateContextResponse, steel_context, path=["response"])

    @parametrize
    async def test_method_create_context_with_all_params(self, async_client: AsyncSteel) -> None:
        steel_context = await async_client.steel_browser.steel_session.steel_context.create_context(
            proxy="proxy",
        )
        assert_matches_type(SteelContextCreateContextResponse, steel_context, path=["response"])

    @parametrize
    async def test_raw_response_create_context(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.steel_session.steel_context.with_raw_response.create_context()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_context = await response.parse()
        assert_matches_type(SteelContextCreateContextResponse, steel_context, path=["response"])

    @parametrize
    async def test_streaming_response_create_context(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.steel_session.steel_context.with_streaming_response.create_context() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_context = await response.parse()
            assert_matches_type(SteelContextCreateContextResponse, steel_context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_context(self, async_client: AsyncSteel) -> None:
        steel_context = await async_client.steel_browser.steel_session.steel_context.delete_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SteelContextDeleteContextResponse, steel_context, path=["response"])

    @parametrize
    async def test_raw_response_delete_context(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.steel_session.steel_context.with_raw_response.delete_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_context = await response.parse()
        assert_matches_type(SteelContextDeleteContextResponse, steel_context, path=["response"])

    @parametrize
    async def test_streaming_response_delete_context(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.steel_session.steel_context.with_streaming_response.delete_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_context = await response.parse()
            assert_matches_type(SteelContextDeleteContextResponse, steel_context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_context(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.steel_browser.steel_session.steel_context.with_raw_response.delete_context(
                "",
            )

    @parametrize
    async def test_method_get_context_data(self, async_client: AsyncSteel) -> None:
        steel_context = await async_client.steel_browser.steel_session.steel_context.get_context_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Context, steel_context, path=["response"])

    @parametrize
    async def test_raw_response_get_context_data(self, async_client: AsyncSteel) -> None:
        response = await async_client.steel_browser.steel_session.steel_context.with_raw_response.get_context_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        steel_context = await response.parse()
        assert_matches_type(Context, steel_context, path=["response"])

    @parametrize
    async def test_streaming_response_get_context_data(self, async_client: AsyncSteel) -> None:
        async with async_client.steel_browser.steel_session.steel_context.with_streaming_response.get_context_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            steel_context = await response.parse()
            assert_matches_type(Context, steel_context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_context_data(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.steel_browser.steel_session.steel_context.with_raw_response.get_context_data(
                "",
            )
