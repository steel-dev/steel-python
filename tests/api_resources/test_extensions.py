# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import (
    ExtensionListResponse,
    ExtensionDeleteResponse,
    ExtensionUpdateResponse,
    ExtensionUploadResponse,
    ExtensionDeleteAllResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtensions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Steel) -> None:
        extension = client.extensions.update(
            extension_id="extensionId",
        )
        assert_matches_type(ExtensionUpdateResponse, extension, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Steel) -> None:
        extension = client.extensions.update(
            extension_id="extensionId",
            file={},
            url="https://example.com",
        )
        assert_matches_type(ExtensionUpdateResponse, extension, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Steel) -> None:
        response = client.extensions.with_raw_response.update(
            extension_id="extensionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = response.parse()
        assert_matches_type(ExtensionUpdateResponse, extension, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Steel) -> None:
        with client.extensions.with_streaming_response.update(
            extension_id="extensionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = response.parse()
            assert_matches_type(ExtensionUpdateResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extension_id` but received ''"):
            client.extensions.with_raw_response.update(
                extension_id="",
            )

    @parametrize
    def test_method_list(self, client: Steel) -> None:
        extension = client.extensions.list()
        assert_matches_type(ExtensionListResponse, extension, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Steel) -> None:
        response = client.extensions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = response.parse()
        assert_matches_type(ExtensionListResponse, extension, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Steel) -> None:
        with client.extensions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = response.parse()
            assert_matches_type(ExtensionListResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Steel) -> None:
        extension = client.extensions.delete(
            "extensionId",
        )
        assert_matches_type(ExtensionDeleteResponse, extension, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Steel) -> None:
        response = client.extensions.with_raw_response.delete(
            "extensionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = response.parse()
        assert_matches_type(ExtensionDeleteResponse, extension, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Steel) -> None:
        with client.extensions.with_streaming_response.delete(
            "extensionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = response.parse()
            assert_matches_type(ExtensionDeleteResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extension_id` but received ''"):
            client.extensions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_delete_all(self, client: Steel) -> None:
        extension = client.extensions.delete_all()
        assert_matches_type(ExtensionDeleteAllResponse, extension, path=["response"])

    @parametrize
    def test_raw_response_delete_all(self, client: Steel) -> None:
        response = client.extensions.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = response.parse()
        assert_matches_type(ExtensionDeleteAllResponse, extension, path=["response"])

    @parametrize
    def test_streaming_response_delete_all(self, client: Steel) -> None:
        with client.extensions.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = response.parse()
            assert_matches_type(ExtensionDeleteAllResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_download(self, client: Steel) -> None:
        extension = client.extensions.download(
            "extensionId",
        )
        assert_matches_type(str, extension, path=["response"])

    @parametrize
    def test_raw_response_download(self, client: Steel) -> None:
        response = client.extensions.with_raw_response.download(
            "extensionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = response.parse()
        assert_matches_type(str, extension, path=["response"])

    @parametrize
    def test_streaming_response_download(self, client: Steel) -> None:
        with client.extensions.with_streaming_response.download(
            "extensionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = response.parse()
            assert_matches_type(str, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_download(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extension_id` but received ''"):
            client.extensions.with_raw_response.download(
                "",
            )

    @parametrize
    def test_method_upload(self, client: Steel) -> None:
        extension = client.extensions.upload()
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Steel) -> None:
        extension = client.extensions.upload(
            file={},
            url="https://example.com",
        )
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Steel) -> None:
        response = client.extensions.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = response.parse()
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Steel) -> None:
        with client.extensions.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = response.parse()
            assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtensions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncSteel) -> None:
        extension = await async_client.extensions.update(
            extension_id="extensionId",
        )
        assert_matches_type(ExtensionUpdateResponse, extension, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSteel) -> None:
        extension = await async_client.extensions.update(
            extension_id="extensionId",
            file={},
            url="https://example.com",
        )
        assert_matches_type(ExtensionUpdateResponse, extension, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSteel) -> None:
        response = await async_client.extensions.with_raw_response.update(
            extension_id="extensionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = await response.parse()
        assert_matches_type(ExtensionUpdateResponse, extension, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSteel) -> None:
        async with async_client.extensions.with_streaming_response.update(
            extension_id="extensionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = await response.parse()
            assert_matches_type(ExtensionUpdateResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extension_id` but received ''"):
            await async_client.extensions.with_raw_response.update(
                extension_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSteel) -> None:
        extension = await async_client.extensions.list()
        assert_matches_type(ExtensionListResponse, extension, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSteel) -> None:
        response = await async_client.extensions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = await response.parse()
        assert_matches_type(ExtensionListResponse, extension, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSteel) -> None:
        async with async_client.extensions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = await response.parse()
            assert_matches_type(ExtensionListResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSteel) -> None:
        extension = await async_client.extensions.delete(
            "extensionId",
        )
        assert_matches_type(ExtensionDeleteResponse, extension, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSteel) -> None:
        response = await async_client.extensions.with_raw_response.delete(
            "extensionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = await response.parse()
        assert_matches_type(ExtensionDeleteResponse, extension, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSteel) -> None:
        async with async_client.extensions.with_streaming_response.delete(
            "extensionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = await response.parse()
            assert_matches_type(ExtensionDeleteResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extension_id` but received ''"):
            await async_client.extensions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_delete_all(self, async_client: AsyncSteel) -> None:
        extension = await async_client.extensions.delete_all()
        assert_matches_type(ExtensionDeleteAllResponse, extension, path=["response"])

    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncSteel) -> None:
        response = await async_client.extensions.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = await response.parse()
        assert_matches_type(ExtensionDeleteAllResponse, extension, path=["response"])

    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncSteel) -> None:
        async with async_client.extensions.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = await response.parse()
            assert_matches_type(ExtensionDeleteAllResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_download(self, async_client: AsyncSteel) -> None:
        extension = await async_client.extensions.download(
            "extensionId",
        )
        assert_matches_type(str, extension, path=["response"])

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncSteel) -> None:
        response = await async_client.extensions.with_raw_response.download(
            "extensionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = await response.parse()
        assert_matches_type(str, extension, path=["response"])

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncSteel) -> None:
        async with async_client.extensions.with_streaming_response.download(
            "extensionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = await response.parse()
            assert_matches_type(str, extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_download(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extension_id` but received ''"):
            await async_client.extensions.with_raw_response.download(
                "",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncSteel) -> None:
        extension = await async_client.extensions.upload()
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncSteel) -> None:
        extension = await async_client.extensions.upload(
            file={},
            url="https://example.com",
        )
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncSteel) -> None:
        response = await async_client.extensions.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extension = await response.parse()
        assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncSteel) -> None:
        async with async_client.extensions.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extension = await response.parse()
            assert_matches_type(ExtensionUploadResponse, extension, path=["response"])

        assert cast(Any, response.is_closed) is True
