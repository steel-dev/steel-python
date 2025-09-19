# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sessions import captcha_solve_image_params
from ...types.sessions.captcha_status_response import CaptchaStatusResponse
from ...types.sessions.captcha_solve_image_response import CaptchaSolveImageResponse

__all__ = ["CaptchasResource", "AsyncCaptchasResource"]


class CaptchasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CaptchasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return CaptchasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CaptchasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return CaptchasResourceWithStreamingResponse(self)

    def solve_image(
        self,
        session_id: str,
        *,
        image_x_path: str,
        input_x_path: str,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptchaSolveImageResponse:
        """
        Solves an image captcha using XPath selectors

        Args:
          image_x_path: XPath to the captcha image element

          input_x_path: XPath to the captcha input element

          url: URL where the captcha is located. Defaults to the current page URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/v1/sessions/{session_id}/captchas/solve-image",
            body=maybe_transform(
                {
                    "image_x_path": image_x_path,
                    "input_x_path": input_x_path,
                    "url": url,
                },
                captcha_solve_image_params.CaptchaSolveImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptchaSolveImageResponse,
        )

    def status(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptchaStatusResponse:
        """
        Gets the current captcha status for a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/v1/sessions/{session_id}/captchas/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptchaStatusResponse,
        )


class AsyncCaptchasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCaptchasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCaptchasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCaptchasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return AsyncCaptchasResourceWithStreamingResponse(self)

    async def solve_image(
        self,
        session_id: str,
        *,
        image_x_path: str,
        input_x_path: str,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptchaSolveImageResponse:
        """
        Solves an image captcha using XPath selectors

        Args:
          image_x_path: XPath to the captcha image element

          input_x_path: XPath to the captcha input element

          url: URL where the captcha is located. Defaults to the current page URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/v1/sessions/{session_id}/captchas/solve-image",
            body=await async_maybe_transform(
                {
                    "image_x_path": image_x_path,
                    "input_x_path": input_x_path,
                    "url": url,
                },
                captcha_solve_image_params.CaptchaSolveImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptchaSolveImageResponse,
        )

    async def status(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptchaStatusResponse:
        """
        Gets the current captcha status for a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/v1/sessions/{session_id}/captchas/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptchaStatusResponse,
        )


class CaptchasResourceWithRawResponse:
    def __init__(self, captchas: CaptchasResource) -> None:
        self._captchas = captchas

        self.solve_image = to_raw_response_wrapper(
            captchas.solve_image,
        )
        self.status = to_raw_response_wrapper(
            captchas.status,
        )


class AsyncCaptchasResourceWithRawResponse:
    def __init__(self, captchas: AsyncCaptchasResource) -> None:
        self._captchas = captchas

        self.solve_image = async_to_raw_response_wrapper(
            captchas.solve_image,
        )
        self.status = async_to_raw_response_wrapper(
            captchas.status,
        )


class CaptchasResourceWithStreamingResponse:
    def __init__(self, captchas: CaptchasResource) -> None:
        self._captchas = captchas

        self.solve_image = to_streamed_response_wrapper(
            captchas.solve_image,
        )
        self.status = to_streamed_response_wrapper(
            captchas.status,
        )


class AsyncCaptchasResourceWithStreamingResponse:
    def __init__(self, captchas: AsyncCaptchasResource) -> None:
        self._captchas = captchas

        self.solve_image = async_to_streamed_response_wrapper(
            captchas.solve_image,
        )
        self.status = async_to_streamed_response_wrapper(
            captchas.status,
        )
