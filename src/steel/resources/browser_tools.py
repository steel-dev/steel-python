# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import browser_tool_pdf_params, browser_tool_scrape_params, browser_tool_screenshot_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.scrape import Scrape

__all__ = ["BrowserToolsResource", "AsyncBrowserToolsResource"]


class BrowserToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowserToolsResourceWithRawResponse:
        return BrowserToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserToolsResourceWithStreamingResponse:
        return BrowserToolsResourceWithStreamingResponse(self)

    def pdf(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Generate a PDF from the specified webpage.

        This endpoint supports bulk
        operations by passing an array of URLs.

        Args:
          url: The URL of the webpage to convert to PDF

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._post(
            "/v1/pdf",
            body=maybe_transform({"url": url}, browser_tool_pdf_params.BrowserToolPdfParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def scrape(
        self,
        *,
        url: str,
        format: List[Literal["html", "cleaned_html", "readability", "markdown"]] | NotGiven = NOT_GIVEN,
        screenshot: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Scrape:
        """Scrape content from a webpage.

        This endpoint supports bulk operations by passing
        an array of URLs. You can specify the desired return type(s) using the 'format'
        parameter and request a screenshot using the 'screenshot' flag.

        Args:
          url: The URL of the webpage to scrape

          format: The desired format(s) for the scraped content

          screenshot: Flag to include a screenshot of the page in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/scrape",
            body=maybe_transform(
                {
                    "url": url,
                    "format": format,
                    "screenshot": screenshot,
                },
                browser_tool_scrape_params.BrowserToolScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Scrape,
        )

    def screenshot(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Capture a screenshot of the specified webpage.

        This endpoint supports bulk
        operations by passing an array of URLs.

        Args:
          url: The URL of the webpage to screenshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return self._post(
            "/v1/screenshot",
            body=maybe_transform({"url": url}, browser_tool_screenshot_params.BrowserToolScreenshotParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncBrowserToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrowserToolsResourceWithRawResponse:
        return AsyncBrowserToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserToolsResourceWithStreamingResponse:
        return AsyncBrowserToolsResourceWithStreamingResponse(self)

    async def pdf(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Generate a PDF from the specified webpage.

        This endpoint supports bulk
        operations by passing an array of URLs.

        Args:
          url: The URL of the webpage to convert to PDF

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._post(
            "/v1/pdf",
            body=await async_maybe_transform({"url": url}, browser_tool_pdf_params.BrowserToolPdfParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def scrape(
        self,
        *,
        url: str,
        format: List[Literal["html", "cleaned_html", "readability", "markdown"]] | NotGiven = NOT_GIVEN,
        screenshot: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Scrape:
        """Scrape content from a webpage.

        This endpoint supports bulk operations by passing
        an array of URLs. You can specify the desired return type(s) using the 'format'
        parameter and request a screenshot using the 'screenshot' flag.

        Args:
          url: The URL of the webpage to scrape

          format: The desired format(s) for the scraped content

          screenshot: Flag to include a screenshot of the page in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/scrape",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "format": format,
                    "screenshot": screenshot,
                },
                browser_tool_scrape_params.BrowserToolScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Scrape,
        )

    async def screenshot(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Capture a screenshot of the specified webpage.

        This endpoint supports bulk
        operations by passing an array of URLs.

        Args:
          url: The URL of the webpage to screenshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return await self._post(
            "/v1/screenshot",
            body=await async_maybe_transform({"url": url}, browser_tool_screenshot_params.BrowserToolScreenshotParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class BrowserToolsResourceWithRawResponse:
    def __init__(self, browser_tools: BrowserToolsResource) -> None:
        self._browser_tools = browser_tools

        self.pdf = to_custom_raw_response_wrapper(
            browser_tools.pdf,
            BinaryAPIResponse,
        )
        self.scrape = to_raw_response_wrapper(
            browser_tools.scrape,
        )
        self.screenshot = to_custom_raw_response_wrapper(
            browser_tools.screenshot,
            BinaryAPIResponse,
        )


class AsyncBrowserToolsResourceWithRawResponse:
    def __init__(self, browser_tools: AsyncBrowserToolsResource) -> None:
        self._browser_tools = browser_tools

        self.pdf = async_to_custom_raw_response_wrapper(
            browser_tools.pdf,
            AsyncBinaryAPIResponse,
        )
        self.scrape = async_to_raw_response_wrapper(
            browser_tools.scrape,
        )
        self.screenshot = async_to_custom_raw_response_wrapper(
            browser_tools.screenshot,
            AsyncBinaryAPIResponse,
        )


class BrowserToolsResourceWithStreamingResponse:
    def __init__(self, browser_tools: BrowserToolsResource) -> None:
        self._browser_tools = browser_tools

        self.pdf = to_custom_streamed_response_wrapper(
            browser_tools.pdf,
            StreamedBinaryAPIResponse,
        )
        self.scrape = to_streamed_response_wrapper(
            browser_tools.scrape,
        )
        self.screenshot = to_custom_streamed_response_wrapper(
            browser_tools.screenshot,
            StreamedBinaryAPIResponse,
        )


class AsyncBrowserToolsResourceWithStreamingResponse:
    def __init__(self, browser_tools: AsyncBrowserToolsResource) -> None:
        self._browser_tools = browser_tools

        self.pdf = async_to_custom_streamed_response_wrapper(
            browser_tools.pdf,
            AsyncStreamedBinaryAPIResponse,
        )
        self.scrape = async_to_streamed_response_wrapper(
            browser_tools.scrape,
        )
        self.screenshot = async_to_custom_streamed_response_wrapper(
            browser_tools.screenshot,
            AsyncStreamedBinaryAPIResponse,
        )
