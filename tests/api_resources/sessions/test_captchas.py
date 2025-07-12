# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from tests.utils import assert_matches_type
from steel.types.sessions import CaptchaStatusResponse, CaptchaSolveImageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCaptchas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_solve_image(self, client: Steel) -> None:
        captcha = client.sessions.captchas.solve_image(
            session_id="sessionId",
            image_x_path="imageXPath",
            input_x_path="inputXPath",
        )
        assert_matches_type(CaptchaSolveImageResponse, captcha, path=["response"])

    @parametrize
    def test_method_solve_image_with_all_params(self, client: Steel) -> None:
        captcha = client.sessions.captchas.solve_image(
            session_id="sessionId",
            image_x_path="imageXPath",
            input_x_path="inputXPath",
            url="url",
        )
        assert_matches_type(CaptchaSolveImageResponse, captcha, path=["response"])

    @parametrize
    def test_raw_response_solve_image(self, client: Steel) -> None:
        response = client.sessions.captchas.with_raw_response.solve_image(
            session_id="sessionId",
            image_x_path="imageXPath",
            input_x_path="inputXPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        captcha = response.parse()
        assert_matches_type(CaptchaSolveImageResponse, captcha, path=["response"])

    @parametrize
    def test_streaming_response_solve_image(self, client: Steel) -> None:
        with client.sessions.captchas.with_streaming_response.solve_image(
            session_id="sessionId",
            image_x_path="imageXPath",
            input_x_path="inputXPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            captcha = response.parse()
            assert_matches_type(CaptchaSolveImageResponse, captcha, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_solve_image(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.captchas.with_raw_response.solve_image(
                session_id="",
                image_x_path="imageXPath",
                input_x_path="inputXPath",
            )

    @parametrize
    def test_method_status(self, client: Steel) -> None:
        captcha = client.sessions.captchas.status(
            "sessionId",
        )
        assert_matches_type(CaptchaStatusResponse, captcha, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Steel) -> None:
        response = client.sessions.captchas.with_raw_response.status(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        captcha = response.parse()
        assert_matches_type(CaptchaStatusResponse, captcha, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Steel) -> None:
        with client.sessions.captchas.with_streaming_response.status(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            captcha = response.parse()
            assert_matches_type(CaptchaStatusResponse, captcha, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.captchas.with_raw_response.status(
                "",
            )


class TestAsyncCaptchas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_solve_image(self, async_client: AsyncSteel) -> None:
        captcha = await async_client.sessions.captchas.solve_image(
            session_id="sessionId",
            image_x_path="imageXPath",
            input_x_path="inputXPath",
        )
        assert_matches_type(CaptchaSolveImageResponse, captcha, path=["response"])

    @parametrize
    async def test_method_solve_image_with_all_params(self, async_client: AsyncSteel) -> None:
        captcha = await async_client.sessions.captchas.solve_image(
            session_id="sessionId",
            image_x_path="imageXPath",
            input_x_path="inputXPath",
            url="url",
        )
        assert_matches_type(CaptchaSolveImageResponse, captcha, path=["response"])

    @parametrize
    async def test_raw_response_solve_image(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.captchas.with_raw_response.solve_image(
            session_id="sessionId",
            image_x_path="imageXPath",
            input_x_path="inputXPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        captcha = await response.parse()
        assert_matches_type(CaptchaSolveImageResponse, captcha, path=["response"])

    @parametrize
    async def test_streaming_response_solve_image(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.captchas.with_streaming_response.solve_image(
            session_id="sessionId",
            image_x_path="imageXPath",
            input_x_path="inputXPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            captcha = await response.parse()
            assert_matches_type(CaptchaSolveImageResponse, captcha, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_solve_image(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.captchas.with_raw_response.solve_image(
                session_id="",
                image_x_path="imageXPath",
                input_x_path="inputXPath",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncSteel) -> None:
        captcha = await async_client.sessions.captchas.status(
            "sessionId",
        )
        assert_matches_type(CaptchaStatusResponse, captcha, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.captchas.with_raw_response.status(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        captcha = await response.parse()
        assert_matches_type(CaptchaStatusResponse, captcha, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.captchas.with_streaming_response.status(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            captcha = await response.parse()
            assert_matches_type(CaptchaStatusResponse, captcha, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.captchas.with_raw_response.status(
                "",
            )
