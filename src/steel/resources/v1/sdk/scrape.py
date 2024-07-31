# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

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
from ....types.v1.sdk import scrape_create_params

__all__ = ["ScrapeResource", "AsyncScrapeResource"]


class ScrapeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScrapeResourceWithRawResponse:
        return ScrapeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScrapeResourceWithStreamingResponse:
        return ScrapeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        format: List[Literal["html", "readability"]] | NotGiven = NOT_GIVEN,
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
            "/v1/sdk/scrape/",
            body=maybe_transform(
                {
                    "url": url,
                    "format": format,
                },
                scrape_create_params.ScrapeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncScrapeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScrapeResourceWithRawResponse:
        return AsyncScrapeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScrapeResourceWithStreamingResponse:
        return AsyncScrapeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        format: List[Literal["html", "readability"]] | NotGiven = NOT_GIVEN,
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
            "/v1/sdk/scrape/",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "format": format,
                },
                scrape_create_params.ScrapeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ScrapeResourceWithRawResponse:
    def __init__(self, scrape: ScrapeResource) -> None:
        self._scrape = scrape

        self.create = to_raw_response_wrapper(
            scrape.create,
        )


class AsyncScrapeResourceWithRawResponse:
    def __init__(self, scrape: AsyncScrapeResource) -> None:
        self._scrape = scrape

        self.create = async_to_raw_response_wrapper(
            scrape.create,
        )


class ScrapeResourceWithStreamingResponse:
    def __init__(self, scrape: ScrapeResource) -> None:
        self._scrape = scrape

        self.create = to_streamed_response_wrapper(
            scrape.create,
        )


class AsyncScrapeResourceWithStreamingResponse:
    def __init__(self, scrape: AsyncScrapeResource) -> None:
        self._scrape = scrape

        self.create = async_to_streamed_response_wrapper(
            scrape.create,
        )
