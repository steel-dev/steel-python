# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import Session, ReleaseSessionResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Steel) -> None:
        session = client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Steel) -> None:
        session = client.session.create(
            proxy="proxy",
            region="CA",
            session_context={},
            session_timeout=0,
            solve_captcha=True,
            stealth_mode=True,
            user_agent="userAgent",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Steel) -> None:
        response = client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Steel) -> None:
        with client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_context(self, client: Steel) -> None:
        session = client.session.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, session, path=["response"])

    @parametrize
    def test_raw_response_get_context(self, client: Steel) -> None:
        response = client.session.with_raw_response.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(object, session, path=["response"])

    @parametrize
    def test_streaming_response_get_context(self, client: Steel) -> None:
        with client.session.with_streaming_response.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(object, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_context(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.get_context(
                "",
            )

    @parametrize
    def test_method_get_data(self, client: Steel) -> None:
        session = client.session.get_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_get_data(self, client: Steel) -> None:
        response = client.session.with_raw_response.get_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_get_data(self, client: Steel) -> None:
        with client.session.with_streaming_response.get_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_data(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.get_data(
                "",
            )

    @parametrize
    def test_method_release(self, client: Steel) -> None:
        session = client.session.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ReleaseSessionResponse, session, path=["response"])

    @parametrize
    def test_raw_response_release(self, client: Steel) -> None:
        response = client.session.with_raw_response.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(ReleaseSessionResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_release(self, client: Steel) -> None:
        with client.session.with_streaming_response.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(ReleaseSessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_release(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.release(
                "",
            )


class TestAsyncSession:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSteel) -> None:
        session = await async_client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSteel) -> None:
        session = await async_client.session.create(
            proxy="proxy",
            region="CA",
            session_context={},
            session_timeout=0,
            solve_captcha=True,
            stealth_mode=True,
            user_agent="userAgent",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSteel) -> None:
        response = await async_client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSteel) -> None:
        async with async_client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_context(self, async_client: AsyncSteel) -> None:
        session = await async_client.session.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, session, path=["response"])

    @parametrize
    async def test_raw_response_get_context(self, async_client: AsyncSteel) -> None:
        response = await async_client.session.with_raw_response.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(object, session, path=["response"])

    @parametrize
    async def test_streaming_response_get_context(self, async_client: AsyncSteel) -> None:
        async with async_client.session.with_streaming_response.get_context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(object, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_context(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.get_context(
                "",
            )

    @parametrize
    async def test_method_get_data(self, async_client: AsyncSteel) -> None:
        session = await async_client.session.get_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_get_data(self, async_client: AsyncSteel) -> None:
        response = await async_client.session.with_raw_response.get_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_get_data(self, async_client: AsyncSteel) -> None:
        async with async_client.session.with_streaming_response.get_data(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_data(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.get_data(
                "",
            )

    @parametrize
    async def test_method_release(self, async_client: AsyncSteel) -> None:
        session = await async_client.session.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ReleaseSessionResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_release(self, async_client: AsyncSteel) -> None:
        response = await async_client.session.with_raw_response.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(ReleaseSessionResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncSteel) -> None:
        async with async_client.session.with_streaming_response.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(ReleaseSessionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_release(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.release(
                "",
            )
