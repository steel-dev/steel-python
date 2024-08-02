# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...types import (
    steel_browser_pdf_params,
    steel_browser_scrape_params,
    steel_browser_screenshot_params,
    steel_browser_list_sessions_params,
    steel_browser_create_session_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from .steel_session import (
    SteelSessionResource,
    AsyncSteelSessionResource,
    SteelSessionResourceWithRawResponse,
    AsyncSteelSessionResourceWithRawResponse,
    SteelSessionResourceWithStreamingResponse,
    AsyncSteelSessionResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .steel_session.steel_session import SteelSessionResource, AsyncSteelSessionResource
from ...types.steel_browser.session import Session
from ...types.steel_browser_scrape_response import SteelBrowserScrapeResponse
from ...types.steel_browser_list_sessions_response import SteelBrowserListSessionsResponse

__all__ = ["SteelBrowserResource", "AsyncSteelBrowserResource"]


class SteelBrowserResource(SyncAPIResource):
    @cached_property
    def steel_session(self) -> SteelSessionResource:
        return SteelSessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> SteelBrowserResourceWithRawResponse:
        return SteelBrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SteelBrowserResourceWithStreamingResponse:
        return SteelBrowserResourceWithStreamingResponse(self)

    def create_session(
        self,
        *,
        org_id: str,
        orgid: str,
        context_data: object | NotGiven = NOT_GIVEN,
        proxy: str | NotGiven = NOT_GIVEN,
        region: Literal["CA", "US", "FR"] | NotGiven = NOT_GIVEN,
        solve_captcha: bool | NotGiven = NOT_GIVEN,
        user_agent: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Start a new browser session for the organization

        Args:
          org_id: Unique identifier for the organization creating the session

          context_data: Custom user context data for the session

          proxy: Proxy configuration for the browser session

          region: Region for the browser session

          solve_captcha: Flag to enable automatic captcha solving

          user_agent: Custom user agent string for the browser session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return self._post(
            "/v1/sessions",
            body=maybe_transform(
                {
                    "org_id": org_id,
                    "context_data": context_data,
                    "proxy": proxy,
                    "region": region,
                    "solve_captcha": solve_captcha,
                    "user_agent": user_agent,
                },
                steel_browser_create_session_params.SteelBrowserCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def list_sessions(
        self,
        *,
        orgid: str,
        live_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SteelBrowserListSessionsResponse:
        """
        Get a list of browser sessions for the organization

        Args:
          live_only: Flag to retrieve only live sessions (default: true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return self._get(
            "/v1/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"live_only": live_only}, steel_browser_list_sessions_params.SteelBrowserListSessionsParams
                ),
            ),
            cast_to=SteelBrowserListSessionsResponse,
        )

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
            body=maybe_transform({"url": url}, steel_browser_pdf_params.SteelBrowserPdfParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def retrieve_session(
        self,
        id: str,
        *,
        orgid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Get detailed information about a specific browser session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return self._get(
            f"/v1/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def scrape(
        self,
        *,
        url: str,
        orgid: str,
        format: List[Literal["html", "cleaned_html", "readability", "markdown"]] | NotGiven = NOT_GIVEN,
        screenshot: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SteelBrowserScrapeResponse:
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
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return self._post(
            "/v1/scrape",
            body=maybe_transform(
                {
                    "url": url,
                    "format": format,
                    "screenshot": screenshot,
                },
                steel_browser_scrape_params.SteelBrowserScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SteelBrowserScrapeResponse,
        )

    def screenshot(
        self,
        *,
        url: str,
        orgid: str,
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
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return self._post(
            "/v1/screenshot",
            body=maybe_transform({"url": url}, steel_browser_screenshot_params.SteelBrowserScreenshotParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSteelBrowserResource(AsyncAPIResource):
    @cached_property
    def steel_session(self) -> AsyncSteelSessionResource:
        return AsyncSteelSessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSteelBrowserResourceWithRawResponse:
        return AsyncSteelBrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSteelBrowserResourceWithStreamingResponse:
        return AsyncSteelBrowserResourceWithStreamingResponse(self)

    async def create_session(
        self,
        *,
        org_id: str,
        orgid: str,
        context_data: object | NotGiven = NOT_GIVEN,
        proxy: str | NotGiven = NOT_GIVEN,
        region: Literal["CA", "US", "FR"] | NotGiven = NOT_GIVEN,
        solve_captcha: bool | NotGiven = NOT_GIVEN,
        user_agent: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Start a new browser session for the organization

        Args:
          org_id: Unique identifier for the organization creating the session

          context_data: Custom user context data for the session

          proxy: Proxy configuration for the browser session

          region: Region for the browser session

          solve_captcha: Flag to enable automatic captcha solving

          user_agent: Custom user agent string for the browser session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return await self._post(
            "/v1/sessions",
            body=await async_maybe_transform(
                {
                    "org_id": org_id,
                    "context_data": context_data,
                    "proxy": proxy,
                    "region": region,
                    "solve_captcha": solve_captcha,
                    "user_agent": user_agent,
                },
                steel_browser_create_session_params.SteelBrowserCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def list_sessions(
        self,
        *,
        orgid: str,
        live_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SteelBrowserListSessionsResponse:
        """
        Get a list of browser sessions for the organization

        Args:
          live_only: Flag to retrieve only live sessions (default: true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return await self._get(
            "/v1/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"live_only": live_only}, steel_browser_list_sessions_params.SteelBrowserListSessionsParams
                ),
            ),
            cast_to=SteelBrowserListSessionsResponse,
        )

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
            body=await async_maybe_transform({"url": url}, steel_browser_pdf_params.SteelBrowserPdfParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def retrieve_session(
        self,
        id: str,
        *,
        orgid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Get detailed information about a specific browser session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return await self._get(
            f"/v1/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def scrape(
        self,
        *,
        url: str,
        orgid: str,
        format: List[Literal["html", "cleaned_html", "readability", "markdown"]] | NotGiven = NOT_GIVEN,
        screenshot: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SteelBrowserScrapeResponse:
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
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return await self._post(
            "/v1/scrape",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "format": format,
                    "screenshot": screenshot,
                },
                steel_browser_scrape_params.SteelBrowserScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SteelBrowserScrapeResponse,
        )

    async def screenshot(
        self,
        *,
        url: str,
        orgid: str,
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
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return await self._post(
            "/v1/screenshot",
            body=await async_maybe_transform(
                {"url": url}, steel_browser_screenshot_params.SteelBrowserScreenshotParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SteelBrowserResourceWithRawResponse:
    def __init__(self, steel_browser: SteelBrowserResource) -> None:
        self._steel_browser = steel_browser

        self.create_session = to_raw_response_wrapper(
            steel_browser.create_session,
        )
        self.list_sessions = to_raw_response_wrapper(
            steel_browser.list_sessions,
        )
        self.pdf = to_custom_raw_response_wrapper(
            steel_browser.pdf,
            BinaryAPIResponse,
        )
        self.retrieve_session = to_raw_response_wrapper(
            steel_browser.retrieve_session,
        )
        self.scrape = to_raw_response_wrapper(
            steel_browser.scrape,
        )
        self.screenshot = to_custom_raw_response_wrapper(
            steel_browser.screenshot,
            BinaryAPIResponse,
        )

    @cached_property
    def steel_session(self) -> SteelSessionResourceWithRawResponse:
        return SteelSessionResourceWithRawResponse(self._steel_browser.steel_session)


class AsyncSteelBrowserResourceWithRawResponse:
    def __init__(self, steel_browser: AsyncSteelBrowserResource) -> None:
        self._steel_browser = steel_browser

        self.create_session = async_to_raw_response_wrapper(
            steel_browser.create_session,
        )
        self.list_sessions = async_to_raw_response_wrapper(
            steel_browser.list_sessions,
        )
        self.pdf = async_to_custom_raw_response_wrapper(
            steel_browser.pdf,
            AsyncBinaryAPIResponse,
        )
        self.retrieve_session = async_to_raw_response_wrapper(
            steel_browser.retrieve_session,
        )
        self.scrape = async_to_raw_response_wrapper(
            steel_browser.scrape,
        )
        self.screenshot = async_to_custom_raw_response_wrapper(
            steel_browser.screenshot,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def steel_session(self) -> AsyncSteelSessionResourceWithRawResponse:
        return AsyncSteelSessionResourceWithRawResponse(self._steel_browser.steel_session)


class SteelBrowserResourceWithStreamingResponse:
    def __init__(self, steel_browser: SteelBrowserResource) -> None:
        self._steel_browser = steel_browser

        self.create_session = to_streamed_response_wrapper(
            steel_browser.create_session,
        )
        self.list_sessions = to_streamed_response_wrapper(
            steel_browser.list_sessions,
        )
        self.pdf = to_custom_streamed_response_wrapper(
            steel_browser.pdf,
            StreamedBinaryAPIResponse,
        )
        self.retrieve_session = to_streamed_response_wrapper(
            steel_browser.retrieve_session,
        )
        self.scrape = to_streamed_response_wrapper(
            steel_browser.scrape,
        )
        self.screenshot = to_custom_streamed_response_wrapper(
            steel_browser.screenshot,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def steel_session(self) -> SteelSessionResourceWithStreamingResponse:
        return SteelSessionResourceWithStreamingResponse(self._steel_browser.steel_session)


class AsyncSteelBrowserResourceWithStreamingResponse:
    def __init__(self, steel_browser: AsyncSteelBrowserResource) -> None:
        self._steel_browser = steel_browser

        self.create_session = async_to_streamed_response_wrapper(
            steel_browser.create_session,
        )
        self.list_sessions = async_to_streamed_response_wrapper(
            steel_browser.list_sessions,
        )
        self.pdf = async_to_custom_streamed_response_wrapper(
            steel_browser.pdf,
            AsyncStreamedBinaryAPIResponse,
        )
        self.retrieve_session = async_to_streamed_response_wrapper(
            steel_browser.retrieve_session,
        )
        self.scrape = async_to_streamed_response_wrapper(
            steel_browser.scrape,
        )
        self.screenshot = async_to_custom_streamed_response_wrapper(
            steel_browser.screenshot,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def steel_session(self) -> AsyncSteelSessionResourceWithStreamingResponse:
        return AsyncSteelSessionResourceWithStreamingResponse(self._steel_browser.steel_session)
