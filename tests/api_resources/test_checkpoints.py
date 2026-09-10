# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import Computer, Checkpoint, CheckpointList
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Steel) -> None:
        checkpoint = client.checkpoints.retrieve(
            "x",
        )
        assert_matches_type(Checkpoint, checkpoint, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Steel) -> None:
        response = client.checkpoints.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = response.parse()
        assert_matches_type(Checkpoint, checkpoint, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Steel) -> None:
        with client.checkpoints.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = response.parse()
            assert_matches_type(Checkpoint, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkpoints.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Steel) -> None:
        checkpoint = client.checkpoints.list()
        assert_matches_type(CheckpointList, checkpoint, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Steel) -> None:
        response = client.checkpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = response.parse()
        assert_matches_type(CheckpointList, checkpoint, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Steel) -> None:
        with client.checkpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = response.parse()
            assert_matches_type(CheckpointList, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Steel) -> None:
        checkpoint = client.checkpoints.delete(
            "x",
        )
        assert_matches_type(Checkpoint, checkpoint, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Steel) -> None:
        response = client.checkpoints.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = response.parse()
        assert_matches_type(Checkpoint, checkpoint, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Steel) -> None:
        with client.checkpoints.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = response.parse()
            assert_matches_type(Checkpoint, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkpoints.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_restore(self, client: Steel) -> None:
        checkpoint = client.checkpoints.restore(
            id="x",
        )
        assert_matches_type(Computer, checkpoint, path=["response"])

    @parametrize
    def test_method_restore_with_all_params(self, client: Steel) -> None:
        checkpoint = client.checkpoints.restore(
            id="x",
            auto_pause=True,
            timeout_seconds=1,
        )
        assert_matches_type(Computer, checkpoint, path=["response"])

    @parametrize
    def test_raw_response_restore(self, client: Steel) -> None:
        response = client.checkpoints.with_raw_response.restore(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = response.parse()
        assert_matches_type(Computer, checkpoint, path=["response"])

    @parametrize
    def test_streaming_response_restore(self, client: Steel) -> None:
        with client.checkpoints.with_streaming_response.restore(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = response.parse()
            assert_matches_type(Computer, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_restore(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkpoints.with_raw_response.restore(
                id="",
            )


class TestAsyncCheckpoints:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSteel) -> None:
        checkpoint = await async_client.checkpoints.retrieve(
            "x",
        )
        assert_matches_type(Checkpoint, checkpoint, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSteel) -> None:
        response = await async_client.checkpoints.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = await response.parse()
        assert_matches_type(Checkpoint, checkpoint, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSteel) -> None:
        async with async_client.checkpoints.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = await response.parse()
            assert_matches_type(Checkpoint, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkpoints.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSteel) -> None:
        checkpoint = await async_client.checkpoints.list()
        assert_matches_type(CheckpointList, checkpoint, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSteel) -> None:
        response = await async_client.checkpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = await response.parse()
        assert_matches_type(CheckpointList, checkpoint, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSteel) -> None:
        async with async_client.checkpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = await response.parse()
            assert_matches_type(CheckpointList, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSteel) -> None:
        checkpoint = await async_client.checkpoints.delete(
            "x",
        )
        assert_matches_type(Checkpoint, checkpoint, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSteel) -> None:
        response = await async_client.checkpoints.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = await response.parse()
        assert_matches_type(Checkpoint, checkpoint, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSteel) -> None:
        async with async_client.checkpoints.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = await response.parse()
            assert_matches_type(Checkpoint, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkpoints.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_restore(self, async_client: AsyncSteel) -> None:
        checkpoint = await async_client.checkpoints.restore(
            id="x",
        )
        assert_matches_type(Computer, checkpoint, path=["response"])

    @parametrize
    async def test_method_restore_with_all_params(self, async_client: AsyncSteel) -> None:
        checkpoint = await async_client.checkpoints.restore(
            id="x",
            auto_pause=True,
            timeout_seconds=1,
        )
        assert_matches_type(Computer, checkpoint, path=["response"])

    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncSteel) -> None:
        response = await async_client.checkpoints.with_raw_response.restore(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = await response.parse()
        assert_matches_type(Computer, checkpoint, path=["response"])

    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncSteel) -> None:
        async with async_client.checkpoints.with_streaming_response.restore(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = await response.parse()
            assert_matches_type(Computer, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_restore(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkpoints.with_raw_response.restore(
                id="",
            )
