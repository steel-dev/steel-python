# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from steel import Steel, AsyncSteel
from tests.utils import assert_matches_type
from steel._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from steel.types.sessions import File, Fileslist, FileDeleteResponse, FileDeleteAllResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Steel) -> None:
        file = client.sessions.files.retrieve(
            file_id="fileId",
            session_id="sessionId",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Steel) -> None:
        response = client.sessions.files.with_raw_response.retrieve(
            file_id="fileId",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Steel) -> None:
        with client.sessions.files.with_streaming_response.retrieve(
            file_id="fileId",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.files.with_raw_response.retrieve(
                file_id="fileId",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.sessions.files.with_raw_response.retrieve(
                file_id="",
                session_id="sessionId",
            )

    @parametrize
    def test_method_list(self, client: Steel) -> None:
        file = client.sessions.files.list(
            "sessionId",
        )
        assert_matches_type(Fileslist, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Steel) -> None:
        response = client.sessions.files.with_raw_response.list(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(Fileslist, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Steel) -> None:
        with client.sessions.files.with_streaming_response.list(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(Fileslist, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.files.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Steel) -> None:
        file = client.sessions.files.delete(
            file_id="fileId",
            session_id="sessionId",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Steel) -> None:
        response = client.sessions.files.with_raw_response.delete(
            file_id="fileId",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Steel) -> None:
        with client.sessions.files.with_streaming_response.delete(
            file_id="fileId",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.files.with_raw_response.delete(
                file_id="fileId",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.sessions.files.with_raw_response.delete(
                file_id="",
                session_id="sessionId",
            )

    @parametrize
    def test_method_delete_all(self, client: Steel) -> None:
        file = client.sessions.files.delete_all(
            "sessionId",
        )
        assert_matches_type(FileDeleteAllResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete_all(self, client: Steel) -> None:
        response = client.sessions.files.with_raw_response.delete_all(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteAllResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete_all(self, client: Steel) -> None:
        with client.sessions.files.with_streaming_response.delete_all(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteAllResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_all(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.files.with_raw_response.delete_all(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/sessionId/files/fileId/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        file = client.sessions.files.download(
            file_id="fileId",
            session_id="sessionId",
        )
        assert file.is_closed
        assert file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/sessionId/files/fileId/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        file = client.sessions.files.with_raw_response.download(
            file_id="fileId",
            session_id="sessionId",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert file.json() == {"foo": "bar"}
        assert isinstance(file, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Steel, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/sessionId/files/fileId/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.sessions.files.with_streaming_response.download(
            file_id="fileId",
            session_id="sessionId",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, StreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.files.with_raw_response.download(
                file_id="fileId",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.sessions.files.with_raw_response.download(
                file_id="",
                session_id="sessionId",
            )

    @parametrize
    def test_method_upload(self, client: Steel) -> None:
        file = client.sessions.files.upload(
            session_id="sessionId",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Steel) -> None:
        file = client.sessions.files.upload(
            session_id="sessionId",
            file={},
            file_url="https://example.com",
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Steel) -> None:
        response = client.sessions.files.with_raw_response.upload(
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Steel) -> None:
        with client.sessions.files.with_streaming_response.upload(
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.files.with_raw_response.upload(
                session_id="",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSteel) -> None:
        file = await async_client.sessions.files.retrieve(
            file_id="fileId",
            session_id="sessionId",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.files.with_raw_response.retrieve(
            file_id="fileId",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.files.with_streaming_response.retrieve(
            file_id="fileId",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.files.with_raw_response.retrieve(
                file_id="fileId",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.sessions.files.with_raw_response.retrieve(
                file_id="",
                session_id="sessionId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSteel) -> None:
        file = await async_client.sessions.files.list(
            "sessionId",
        )
        assert_matches_type(Fileslist, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.files.with_raw_response.list(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(Fileslist, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.files.with_streaming_response.list(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(Fileslist, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.files.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSteel) -> None:
        file = await async_client.sessions.files.delete(
            file_id="fileId",
            session_id="sessionId",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.files.with_raw_response.delete(
            file_id="fileId",
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.files.with_streaming_response.delete(
            file_id="fileId",
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.files.with_raw_response.delete(
                file_id="fileId",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.sessions.files.with_raw_response.delete(
                file_id="",
                session_id="sessionId",
            )

    @parametrize
    async def test_method_delete_all(self, async_client: AsyncSteel) -> None:
        file = await async_client.sessions.files.delete_all(
            "sessionId",
        )
        assert_matches_type(FileDeleteAllResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.files.with_raw_response.delete_all(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteAllResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.files.with_streaming_response.delete_all(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteAllResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.files.with_raw_response.delete_all(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/sessionId/files/fileId/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        file = await async_client.sessions.files.download(
            file_id="fileId",
            session_id="sessionId",
        )
        assert file.is_closed
        assert await file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/sessionId/files/fileId/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        file = await async_client.sessions.files.with_raw_response.download(
            file_id="fileId",
            session_id="sessionId",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await file.json() == {"foo": "bar"}
        assert isinstance(file, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncSteel, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sessions/sessionId/files/fileId/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.sessions.files.with_streaming_response.download(
            file_id="fileId",
            session_id="sessionId",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.files.with_raw_response.download(
                file_id="fileId",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.sessions.files.with_raw_response.download(
                file_id="",
                session_id="sessionId",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncSteel) -> None:
        file = await async_client.sessions.files.upload(
            session_id="sessionId",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncSteel) -> None:
        file = await async_client.sessions.files.upload(
            session_id="sessionId",
            file={},
            file_url="https://example.com",
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.files.with_raw_response.upload(
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.files.with_streaming_response.upload(
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.files.with_raw_response.upload(
                session_id="",
            )
