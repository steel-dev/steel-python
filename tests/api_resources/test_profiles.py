# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import (
    ProfileGetResponse,
    ProfileListResponse,
    ProfileCreateResponse,
    ProfileUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Steel) -> None:
        profile = client.profiles.create(
            user_data_dir=b"raw file contents",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Steel) -> None:
        profile = client.profiles.create(
            user_data_dir=b"raw file contents",
            dimensions={
                "height": 0,
                "width": 0,
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Steel) -> None:
        response = client.profiles.with_raw_response.create(
            user_data_dir=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Steel) -> None:
        with client.profiles.with_streaming_response.create(
            user_data_dir=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Steel) -> None:
        profile = client.profiles.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_data_dir=b"raw file contents",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Steel) -> None:
        profile = client.profiles.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_data_dir=b"raw file contents",
            dimensions={
                "height": 0,
                "width": 0,
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Steel) -> None:
        response = client.profiles.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_data_dir=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Steel) -> None:
        with client.profiles.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_data_dir=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.profiles.with_raw_response.update(
                id="",
                user_data_dir=b"raw file contents",
            )

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

    @parametrize
    def test_method_get(self, client: Steel) -> None:
        profile = client.profiles.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileGetResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Steel) -> None:
        response = client.profiles.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileGetResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Steel) -> None:
        with client.profiles.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileGetResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.profiles.with_raw_response.get(
                "",
            )


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSteel) -> None:
        profile = await async_client.profiles.create(
            user_data_dir=b"raw file contents",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSteel) -> None:
        profile = await async_client.profiles.create(
            user_data_dir=b"raw file contents",
            dimensions={
                "height": 0,
                "width": 0,
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSteel) -> None:
        response = await async_client.profiles.with_raw_response.create(
            user_data_dir=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSteel) -> None:
        async with async_client.profiles.with_streaming_response.create(
            user_data_dir=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSteel) -> None:
        profile = await async_client.profiles.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_data_dir=b"raw file contents",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSteel) -> None:
        profile = await async_client.profiles.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_data_dir=b"raw file contents",
            dimensions={
                "height": 0,
                "width": 0,
            },
            proxy_url="https://example.com",
            user_agent="userAgent",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSteel) -> None:
        response = await async_client.profiles.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_data_dir=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSteel) -> None:
        async with async_client.profiles.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_data_dir=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.profiles.with_raw_response.update(
                id="",
                user_data_dir=b"raw file contents",
            )

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

    @parametrize
    async def test_method_get(self, async_client: AsyncSteel) -> None:
        profile = await async_client.profiles.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileGetResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSteel) -> None:
        response = await async_client.profiles.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileGetResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSteel) -> None:
        async with async_client.profiles.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileGetResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.profiles.with_raw_response.get(
                "",
            )
