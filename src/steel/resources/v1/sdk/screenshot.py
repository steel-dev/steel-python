# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.sdk import screenshot_create_params

__all__ = ["ScreenshotResource", "AsyncScreenshotResource"]


class ScreenshotResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScreenshotResourceWithRawResponse:
        return ScreenshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenshotResourceWithStreamingResponse:
        return ScreenshotResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/sdk/screenshot/",
            body=maybe_transform({"url": url}, screenshot_create_params.ScreenshotCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncScreenshotResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScreenshotResourceWithRawResponse:
        return AsyncScreenshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenshotResourceWithStreamingResponse:
        return AsyncScreenshotResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/sdk/screenshot/",
            body=await async_maybe_transform({"url": url}, screenshot_create_params.ScreenshotCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ScreenshotResourceWithRawResponse:
    def __init__(self, screenshot: ScreenshotResource) -> None:
        self._screenshot = screenshot

        self.create = to_raw_response_wrapper(
            screenshot.create,
        )


class AsyncScreenshotResourceWithRawResponse:
    def __init__(self, screenshot: AsyncScreenshotResource) -> None:
        self._screenshot = screenshot

        self.create = async_to_raw_response_wrapper(
            screenshot.create,
        )


class ScreenshotResourceWithStreamingResponse:
    def __init__(self, screenshot: ScreenshotResource) -> None:
        self._screenshot = screenshot

        self.create = to_streamed_response_wrapper(
            screenshot.create,
        )


class AsyncScreenshotResourceWithStreamingResponse:
    def __init__(self, screenshot: AsyncScreenshotResource) -> None:
        self._screenshot = screenshot

        self.create = async_to_streamed_response_wrapper(
            screenshot.create,
        )
