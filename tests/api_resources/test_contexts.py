# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import (
    GetContextResponse,
    GetContextsResponse,
    ContextDeleteResponse,
    CreateContextResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContexts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Steel) -> None:
        context = client.contexts.create()
        assert_matches_type(CreateContextResponse, context, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Steel) -> None:
        context = client.contexts.create(
            proxy="proxy",
        )
        assert_matches_type(CreateContextResponse, context, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Steel) -> None:
        response = client.contexts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(CreateContextResponse, context, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Steel) -> None:
        with client.contexts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(CreateContextResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Steel) -> None:
        context = client.contexts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetContextResponse, context, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Steel) -> None:
        response = client.contexts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(GetContextResponse, context, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Steel) -> None:
        with client.contexts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(GetContextResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contexts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Steel) -> None:
        context = client.contexts.list()
        assert_matches_type(GetContextsResponse, context, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Steel) -> None:
        response = client.contexts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(GetContextsResponse, context, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Steel) -> None:
        with client.contexts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(GetContextsResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Steel) -> None:
        context = client.contexts.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ContextDeleteResponse, context, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Steel) -> None:
        response = client.contexts.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextDeleteResponse, context, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Steel) -> None:
        with client.contexts.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextDeleteResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contexts.with_raw_response.delete(
                "",
            )


class TestAsyncContexts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSteel) -> None:
        context = await async_client.contexts.create()
        assert_matches_type(CreateContextResponse, context, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSteel) -> None:
        context = await async_client.contexts.create(
            proxy="proxy",
        )
        assert_matches_type(CreateContextResponse, context, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSteel) -> None:
        response = await async_client.contexts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(CreateContextResponse, context, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSteel) -> None:
        async with async_client.contexts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(CreateContextResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSteel) -> None:
        context = await async_client.contexts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetContextResponse, context, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSteel) -> None:
        response = await async_client.contexts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(GetContextResponse, context, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSteel) -> None:
        async with async_client.contexts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(GetContextResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contexts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSteel) -> None:
        context = await async_client.contexts.list()
        assert_matches_type(GetContextsResponse, context, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSteel) -> None:
        response = await async_client.contexts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(GetContextsResponse, context, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSteel) -> None:
        async with async_client.contexts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(GetContextsResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSteel) -> None:
        context = await async_client.contexts.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ContextDeleteResponse, context, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSteel) -> None:
        response = await async_client.contexts.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextDeleteResponse, context, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSteel) -> None:
        async with async_client.contexts.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextDeleteResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contexts.with_raw_response.delete(
                "",
            )
