# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import (
    CredentialListResponse,
    CredentialCreateResponse,
    CredentialDeleteResponse,
    CredentialUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Steel) -> None:
        credential = client.credentials.create(
            value={"foo": "string"},
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Steel) -> None:
        credential = client.credentials.create(
            value={"foo": "string"},
            label="label",
            namespace="namespace",
            origin="origin",
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Steel) -> None:
        response = client.credentials.with_raw_response.create(
            value={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Steel) -> None:
        with client.credentials.with_streaming_response.create(
            value={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialCreateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Steel) -> None:
        credential = client.credentials.update()
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Steel) -> None:
        credential = client.credentials.update(
            label="label",
            namespace="namespace",
            origin="origin",
            value={"foo": "string"},
        )
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Steel) -> None:
        response = client.credentials.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Steel) -> None:
        with client.credentials.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Steel) -> None:
        credential = client.credentials.list()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Steel) -> None:
        credential = client.credentials.list(
            namespace="namespace",
            origin="origin",
        )
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Steel) -> None:
        response = client.credentials.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Steel) -> None:
        with client.credentials.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialListResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Steel) -> None:
        credential = client.credentials.delete(
            origin="origin",
        )
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Steel) -> None:
        credential = client.credentials.delete(
            origin="origin",
            namespace="namespace",
        )
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Steel) -> None:
        response = client.credentials.with_raw_response.delete(
            origin="origin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Steel) -> None:
        with client.credentials.with_streaming_response.delete(
            origin="origin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSteel) -> None:
        credential = await async_client.credentials.create(
            value={"foo": "string"},
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSteel) -> None:
        credential = await async_client.credentials.create(
            value={"foo": "string"},
            label="label",
            namespace="namespace",
            origin="origin",
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSteel) -> None:
        response = await async_client.credentials.with_raw_response.create(
            value={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSteel) -> None:
        async with async_client.credentials.with_streaming_response.create(
            value={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialCreateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSteel) -> None:
        credential = await async_client.credentials.update()
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSteel) -> None:
        credential = await async_client.credentials.update(
            label="label",
            namespace="namespace",
            origin="origin",
            value={"foo": "string"},
        )
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSteel) -> None:
        response = await async_client.credentials.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSteel) -> None:
        async with async_client.credentials.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSteel) -> None:
        credential = await async_client.credentials.list()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSteel) -> None:
        credential = await async_client.credentials.list(
            namespace="namespace",
            origin="origin",
        )
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSteel) -> None:
        response = await async_client.credentials.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSteel) -> None:
        async with async_client.credentials.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialListResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSteel) -> None:
        credential = await async_client.credentials.delete(
            origin="origin",
        )
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSteel) -> None:
        credential = await async_client.credentials.delete(
            origin="origin",
            namespace="namespace",
        )
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSteel) -> None:
        response = await async_client.credentials.with_raw_response.delete(
            origin="origin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSteel) -> None:
        async with async_client.credentials.with_streaming_response.delete(
            origin="origin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True
