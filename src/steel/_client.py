# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, Mapping
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_pdf_params, client_scrape_params, client_screenshot_params
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    omit,
    not_given,
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
from .resources import files, profiles, extensions, credentials
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.sessions import sessions
from .types.pdf_response import PdfResponse
from .types.scrape_response import ScrapeResponse
from .types.screenshot_response import ScreenshotResponse

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Steel", "AsyncSteel", "Client", "AsyncClient"]


class Steel(SyncAPIClient):
    credentials: credentials.CredentialsResource
    files: files.FilesResource
    sessions: sessions.SessionsResource
    extensions: extensions.ExtensionsResource
    profiles: profiles.ProfilesResource
    with_raw_response: SteelWithRawResponse
    with_streaming_response: SteelWithStreamedResponse

    # client options
    steel_api_key: str | None

    def __init__(
        self,
        *,
        steel_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

        This automatically infers the `steel_api_key` argument from the `STEEL_API_KEY` environment variable if it is not provided.
        """
        if steel_api_key is None:
            steel_api_key = os.environ.get("STEEL_API_KEY")
        self.steel_api_key = steel_api_key

        if base_url is None:
            base_url = os.environ.get("STEEL_BASE_URL")
        if base_url is None:
            base_url = f"https://api.steel.dev"

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

        self.credentials = credentials.CredentialsResource(self)
        self.files = files.FilesResource(self)
        self.sessions = sessions.SessionsResource(self)
        self.extensions = extensions.ExtensionsResource(self)
        self.profiles = profiles.ProfilesResource(self)
        self.with_raw_response = SteelWithRawResponse(self)
        self.with_streaming_response = SteelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        steel_api_key = self.steel_api_key
        if steel_api_key is None:
            return {}
        return {"steel-api-key": steel_api_key}

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
        steel_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
            steel_api_key=steel_api_key or self.steel_api_key,
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

    def pdf(
        self,
        *,
        url: str,
        delay: float | Omit = omit,
        region: str | Omit = omit,
        use_proxy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PdfResponse:
        """
        Generates a PDF from a specified webpage.

        Args:
          url: URL of the webpage to convert to PDF

          delay: Delay before generating the PDF (in milliseconds)

          region: The desired region for the action to be performed in

          use_proxy: Use a Steel-provided residential proxy for generating the PDF

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/pdf",
            body=maybe_transform(
                {
                    "url": url,
                    "delay": delay,
                    "region": region,
                    "use_proxy": use_proxy,
                },
                client_pdf_params.ClientPdfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PdfResponse,
        )

    def scrape(
        self,
        *,
        url: str,
        delay: float | Omit = omit,
        format: List[Literal["html", "readability", "cleaned_html", "markdown"]] | Omit = omit,
        pdf: bool | Omit = omit,
        region: str | Omit = omit,
        screenshot: bool | Omit = omit,
        use_proxy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScrapeResponse:
        """
        Extracts content from a specified URL.

        Args:
          url: URL of the webpage to scrape

          delay: Delay before scraping (in milliseconds)

          format: Desired format(s) for the scraped content. Default is `html`.

          pdf: Include a PDF in the response

          region: The desired region for the action to be performed in

          screenshot: Include a screenshot in the response

          use_proxy: Use a Steel-provided residential proxy for the scrape

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
                    "delay": delay,
                    "format": format,
                    "pdf": pdf,
                    "region": region,
                    "screenshot": screenshot,
                    "use_proxy": use_proxy,
                },
                client_scrape_params.ClientScrapeParams,
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
        delay: float | Omit = omit,
        full_page: bool | Omit = omit,
        region: str | Omit = omit,
        use_proxy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenshotResponse:
        """
        Captures a screenshot of a specified webpage.

        Args:
          url: URL of the webpage to capture

          delay: Delay before capturing the screenshot (in milliseconds)

          full_page: Capture the full page screenshot. Default is `false`.

          region: The desired region for the action to be performed in

          use_proxy: Use a Steel-provided residential proxy for capturing the screenshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/screenshot",
            body=maybe_transform(
                {
                    "url": url,
                    "delay": delay,
                    "full_page": full_page,
                    "region": region,
                    "use_proxy": use_proxy,
                },
                client_screenshot_params.ClientScreenshotParams,
            ),
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
    credentials: credentials.AsyncCredentialsResource
    files: files.AsyncFilesResource
    sessions: sessions.AsyncSessionsResource
    extensions: extensions.AsyncExtensionsResource
    profiles: profiles.AsyncProfilesResource
    with_raw_response: AsyncSteelWithRawResponse
    with_streaming_response: AsyncSteelWithStreamedResponse

    # client options
    steel_api_key: str | None

    def __init__(
        self,
        *,
        steel_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncSteel client instance.

        This automatically infers the `steel_api_key` argument from the `STEEL_API_KEY` environment variable if it is not provided.
        """
        if steel_api_key is None:
            steel_api_key = os.environ.get("STEEL_API_KEY")
        self.steel_api_key = steel_api_key

        if base_url is None:
            base_url = os.environ.get("STEEL_BASE_URL")
        if base_url is None:
            base_url = f"https://api.steel.dev"

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

        self.credentials = credentials.AsyncCredentialsResource(self)
        self.files = files.AsyncFilesResource(self)
        self.sessions = sessions.AsyncSessionsResource(self)
        self.extensions = extensions.AsyncExtensionsResource(self)
        self.profiles = profiles.AsyncProfilesResource(self)
        self.with_raw_response = AsyncSteelWithRawResponse(self)
        self.with_streaming_response = AsyncSteelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        steel_api_key = self.steel_api_key
        if steel_api_key is None:
            return {}
        return {"steel-api-key": steel_api_key}

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
        steel_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
            steel_api_key=steel_api_key or self.steel_api_key,
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

    async def pdf(
        self,
        *,
        url: str,
        delay: float | Omit = omit,
        region: str | Omit = omit,
        use_proxy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PdfResponse:
        """
        Generates a PDF from a specified webpage.

        Args:
          url: URL of the webpage to convert to PDF

          delay: Delay before generating the PDF (in milliseconds)

          region: The desired region for the action to be performed in

          use_proxy: Use a Steel-provided residential proxy for generating the PDF

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/pdf",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "delay": delay,
                    "region": region,
                    "use_proxy": use_proxy,
                },
                client_pdf_params.ClientPdfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PdfResponse,
        )

    async def scrape(
        self,
        *,
        url: str,
        delay: float | Omit = omit,
        format: List[Literal["html", "readability", "cleaned_html", "markdown"]] | Omit = omit,
        pdf: bool | Omit = omit,
        region: str | Omit = omit,
        screenshot: bool | Omit = omit,
        use_proxy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScrapeResponse:
        """
        Extracts content from a specified URL.

        Args:
          url: URL of the webpage to scrape

          delay: Delay before scraping (in milliseconds)

          format: Desired format(s) for the scraped content. Default is `html`.

          pdf: Include a PDF in the response

          region: The desired region for the action to be performed in

          screenshot: Include a screenshot in the response

          use_proxy: Use a Steel-provided residential proxy for the scrape

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
                    "delay": delay,
                    "format": format,
                    "pdf": pdf,
                    "region": region,
                    "screenshot": screenshot,
                    "use_proxy": use_proxy,
                },
                client_scrape_params.ClientScrapeParams,
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
        delay: float | Omit = omit,
        full_page: bool | Omit = omit,
        region: str | Omit = omit,
        use_proxy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenshotResponse:
        """
        Captures a screenshot of a specified webpage.

        Args:
          url: URL of the webpage to capture

          delay: Delay before capturing the screenshot (in milliseconds)

          full_page: Capture the full page screenshot. Default is `false`.

          region: The desired region for the action to be performed in

          use_proxy: Use a Steel-provided residential proxy for capturing the screenshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/screenshot",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "delay": delay,
                    "full_page": full_page,
                    "region": region,
                    "use_proxy": use_proxy,
                },
                client_screenshot_params.ClientScreenshotParams,
            ),
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
        self.credentials = credentials.CredentialsResourceWithRawResponse(client.credentials)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.sessions = sessions.SessionsResourceWithRawResponse(client.sessions)
        self.extensions = extensions.ExtensionsResourceWithRawResponse(client.extensions)
        self.profiles = profiles.ProfilesResourceWithRawResponse(client.profiles)

        self.pdf = to_raw_response_wrapper(
            client.pdf,
        )
        self.scrape = to_raw_response_wrapper(
            client.scrape,
        )
        self.screenshot = to_raw_response_wrapper(
            client.screenshot,
        )


class AsyncSteelWithRawResponse:
    def __init__(self, client: AsyncSteel) -> None:
        self.credentials = credentials.AsyncCredentialsResourceWithRawResponse(client.credentials)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.sessions = sessions.AsyncSessionsResourceWithRawResponse(client.sessions)
        self.extensions = extensions.AsyncExtensionsResourceWithRawResponse(client.extensions)
        self.profiles = profiles.AsyncProfilesResourceWithRawResponse(client.profiles)

        self.pdf = async_to_raw_response_wrapper(
            client.pdf,
        )
        self.scrape = async_to_raw_response_wrapper(
            client.scrape,
        )
        self.screenshot = async_to_raw_response_wrapper(
            client.screenshot,
        )


class SteelWithStreamedResponse:
    def __init__(self, client: Steel) -> None:
        self.credentials = credentials.CredentialsResourceWithStreamingResponse(client.credentials)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.sessions = sessions.SessionsResourceWithStreamingResponse(client.sessions)
        self.extensions = extensions.ExtensionsResourceWithStreamingResponse(client.extensions)
        self.profiles = profiles.ProfilesResourceWithStreamingResponse(client.profiles)

        self.pdf = to_streamed_response_wrapper(
            client.pdf,
        )
        self.scrape = to_streamed_response_wrapper(
            client.scrape,
        )
        self.screenshot = to_streamed_response_wrapper(
            client.screenshot,
        )


class AsyncSteelWithStreamedResponse:
    def __init__(self, client: AsyncSteel) -> None:
        self.credentials = credentials.AsyncCredentialsResourceWithStreamingResponse(client.credentials)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.sessions = sessions.AsyncSessionsResourceWithStreamingResponse(client.sessions)
        self.extensions = extensions.AsyncExtensionsResourceWithStreamingResponse(client.extensions)
        self.profiles = profiles.AsyncProfilesResourceWithStreamingResponse(client.profiles)

        self.pdf = async_to_streamed_response_wrapper(
            client.pdf,
        )
        self.scrape = async_to_streamed_response_wrapper(
            client.scrape,
        )
        self.screenshot = async_to_streamed_response_wrapper(
            client.screenshot,
        )


Client = Steel

AsyncClient = AsyncSteel
