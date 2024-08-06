# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, Union, Mapping
from typing_extensions import Self, Literal, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from .types import (
    top_level_scrape_params,
    top_level_screenshot_params,
    top_level_generate_pdf_params,
    top_level_list_sessions_params,
)
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from .pagination import SyncCursorPage, AsyncCursorPage
from ._exceptions import SteelError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    AsyncPaginator,
    make_request_options,
)
from .types.session import Session
from .types.pdf_response import PdfResponse
from .types.scrape_response import ScrapeResponse
from .types.screenshot_response import ScreenshotResponse

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Steel",
    "AsyncSteel",
    "Client",
    "AsyncClient",
]


class Steel(SyncAPIClient):
    sessions: resources.SessionsResource
    with_raw_response: SteelWithRawResponse
    with_streaming_response: SteelWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Steel client instance.

        This automatically infers the `api_key` argument from the `STEEL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("STEEL_API_KEY")
        if api_key is None:
            raise SteelError(
                "The api_key client option must be set either by passing api_key to the client or by setting the STEEL_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("STEEL_BASE_URL")
        if base_url is None:
            base_url = f"http://api.steel.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.sessions = resources.SessionsResource(self)
        self.with_raw_response = SteelWithRawResponse(self)
        self.with_streaming_response = SteelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"steel-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def generate_pdf(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PdfResponse:
        """
        Generate a PDF from the specified webpage.

        Args:
          url: The URL of the webpage to convert to PDF

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/pdf",
            body=maybe_transform({"url": url}, top_level_generate_pdf_params.TopLevelGeneratePdfParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PdfResponse,
        )

    def list_sessions(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        live_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Session]:
        """Get a paginated list of browser sessions.

        Use the `next_cursor` from the
        response to fetch the next page of results.

        Args:
          cursor: Cursor for pagination, use the `next_cursor` from the previous response

          limit: Number of sessions to return per request (default: 25, max: 100)

          live_only: Flag to retrieve only live sessions (default: true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v1/sessions",
            page=SyncCursorPage[Session],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "live_only": live_only,
                    },
                    top_level_list_sessions_params.TopLevelListSessionsParams,
                ),
            ),
            model=Session,
        )

    def scrape(
        self,
        *,
        url: str,
        format: List[Literal["html", "cleaned_html", "readability", "markdown"]] | NotGiven = NOT_GIVEN,
        pdf: bool | NotGiven = NOT_GIVEN,
        screenshot: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScrapeResponse:
        """Scrape content from a webpage.

        This endpoint supports specifying the desired
        return type(s) using the 'format' parameter. You can also request a screenshot
        and/or PDF using the 'screenshot' and 'pdf' flags.

        Args:
          url: The URL of the webpage to scrape

          format: The desired format(s) for the scraped content

          pdf: Flag to include a PDF of the page in the response

          screenshot: Flag to include a screenshot of the page in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/scrape",
            body=maybe_transform(
                {
                    "url": url,
                    "format": format,
                    "pdf": pdf,
                    "screenshot": screenshot,
                },
                top_level_scrape_params.TopLevelScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScrapeResponse,
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
    ) -> ScreenshotResponse:
        """
        Capture a screenshot of the specified webpage.

        Args:
          url: The URL of the webpage to screenshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/screenshot",
            body=maybe_transform({"url": url}, top_level_screenshot_params.TopLevelScreenshotParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenshotResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSteel(AsyncAPIClient):
    sessions: resources.AsyncSessionsResource
    with_raw_response: AsyncSteelWithRawResponse
    with_streaming_response: AsyncSteelWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async Steel client instance.

        This automatically infers the `api_key` argument from the `STEEL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("STEEL_API_KEY")
        if api_key is None:
            raise SteelError(
                "The api_key client option must be set either by passing api_key to the client or by setting the STEEL_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("STEEL_BASE_URL")
        if base_url is None:
            base_url = f"http://api.steel.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.sessions = resources.AsyncSessionsResource(self)
        self.with_raw_response = AsyncSteelWithRawResponse(self)
        self.with_streaming_response = AsyncSteelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"steel-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def generate_pdf(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PdfResponse:
        """
        Generate a PDF from the specified webpage.

        Args:
          url: The URL of the webpage to convert to PDF

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/pdf",
            body=await async_maybe_transform({"url": url}, top_level_generate_pdf_params.TopLevelGeneratePdfParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PdfResponse,
        )

    def list_sessions(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        live_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Session, AsyncCursorPage[Session]]:
        """Get a paginated list of browser sessions.

        Use the `next_cursor` from the
        response to fetch the next page of results.

        Args:
          cursor: Cursor for pagination, use the `next_cursor` from the previous response

          limit: Number of sessions to return per request (default: 25, max: 100)

          live_only: Flag to retrieve only live sessions (default: true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get_api_list(
            "/v1/sessions",
            page=AsyncCursorPage[Session],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "live_only": live_only,
                    },
                    top_level_list_sessions_params.TopLevelListSessionsParams,
                ),
            ),
            model=Session,
        )

    async def scrape(
        self,
        *,
        url: str,
        format: List[Literal["html", "cleaned_html", "readability", "markdown"]] | NotGiven = NOT_GIVEN,
        pdf: bool | NotGiven = NOT_GIVEN,
        screenshot: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScrapeResponse:
        """Scrape content from a webpage.

        This endpoint supports specifying the desired
        return type(s) using the 'format' parameter. You can also request a screenshot
        and/or PDF using the 'screenshot' and 'pdf' flags.

        Args:
          url: The URL of the webpage to scrape

          format: The desired format(s) for the scraped content

          pdf: Flag to include a PDF of the page in the response

          screenshot: Flag to include a screenshot of the page in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/scrape",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "format": format,
                    "pdf": pdf,
                    "screenshot": screenshot,
                },
                top_level_scrape_params.TopLevelScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScrapeResponse,
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
    ) -> ScreenshotResponse:
        """
        Capture a screenshot of the specified webpage.

        Args:
          url: The URL of the webpage to screenshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/screenshot",
            body=await async_maybe_transform({"url": url}, top_level_screenshot_params.TopLevelScreenshotParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenshotResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SteelWithRawResponse:
    def __init__(self, client: Steel) -> None:
        self.sessions = resources.SessionsResourceWithRawResponse(client.sessions)

        self.generate_pdf = to_raw_response_wrapper(
            client.generate_pdf,
        )
        self.list_sessions = to_raw_response_wrapper(
            client.list_sessions,
        )
        self.scrape = to_raw_response_wrapper(
            client.scrape,
        )
        self.screenshot = to_raw_response_wrapper(
            client.screenshot,
        )


class AsyncSteelWithRawResponse:
    def __init__(self, client: AsyncSteel) -> None:
        self.sessions = resources.AsyncSessionsResourceWithRawResponse(client.sessions)

        self.generate_pdf = async_to_raw_response_wrapper(
            client.generate_pdf,
        )
        self.list_sessions = async_to_raw_response_wrapper(
            client.list_sessions,
        )
        self.scrape = async_to_raw_response_wrapper(
            client.scrape,
        )
        self.screenshot = async_to_raw_response_wrapper(
            client.screenshot,
        )


class SteelWithStreamedResponse:
    def __init__(self, client: Steel) -> None:
        self.sessions = resources.SessionsResourceWithStreamingResponse(client.sessions)

        self.generate_pdf = to_streamed_response_wrapper(
            client.generate_pdf,
        )
        self.list_sessions = to_streamed_response_wrapper(
            client.list_sessions,
        )
        self.scrape = to_streamed_response_wrapper(
            client.scrape,
        )
        self.screenshot = to_streamed_response_wrapper(
            client.screenshot,
        )


class AsyncSteelWithStreamedResponse:
    def __init__(self, client: AsyncSteel) -> None:
        self.sessions = resources.AsyncSessionsResourceWithStreamingResponse(client.sessions)

        self.generate_pdf = async_to_streamed_response_wrapper(
            client.generate_pdf,
        )
        self.list_sessions = async_to_streamed_response_wrapper(
            client.list_sessions,
        )
        self.scrape = async_to_streamed_response_wrapper(
            client.scrape,
        )
        self.screenshot = async_to_streamed_response_wrapper(
            client.screenshot,
        )


Client = Steel

AsyncClient = AsyncSteel
