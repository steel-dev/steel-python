# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...types import session_list_params, session_create_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .captchas import (
    CaptchasResource,
    AsyncCaptchasResource,
    CaptchasResourceWithRawResponse,
    AsyncCaptchasResourceWithRawResponse,
    CaptchasResourceWithStreamingResponse,
    AsyncCaptchasResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSessionsCursor, AsyncSessionsCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.session import Session as TypesSession
from ...types.sessionslist import Session as SessionslistSession
from ...types.session_context import SessionContext
from ...types.session_events_response import SessionEventsResponse
from ...types.session_release_response import SessionReleaseResponse
from ...types.session_release_all_response import SessionReleaseAllResponse
from ...types.session_live_details_response import SessionLiveDetailsResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def captchas(self) -> CaptchasResource:
        return CaptchasResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        block_ads: bool | Omit = omit,
        concurrency: int | Omit = omit,
        credentials: session_create_params.Credentials | Omit = omit,
        device_config: session_create_params.DeviceConfig | Omit = omit,
        dimensions: session_create_params.Dimensions | Omit = omit,
        extension_ids: SequenceNotStr[str] | Omit = omit,
        headless: bool | Omit = omit,
        is_selenium: bool | Omit = omit,
        namespace: str | Omit = omit,
        optimize_bandwidth: session_create_params.OptimizeBandwidth | Omit = omit,
        persist_profile: bool | Omit = omit,
        profile_id: str | Omit = omit,
        proxy_url: str | Omit = omit,
        region: str | Omit = omit,
        session_context: session_create_params.SessionContext | Omit = omit,
        session_id: str | Omit = omit,
        solve_captcha: bool | Omit = omit,
        stealth_config: session_create_params.StealthConfig | Omit = omit,
        api_timeout: int | Omit = omit,
        use_proxy: session_create_params.UseProxy | Omit = omit,
        user_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypesSession:
        """
        Creates a new session with the provided configuration.

        Args:
          block_ads: Block ads in the browser session. Default is false.

          concurrency: Number of sessions to create concurrently (check your plan limit)

          credentials: Configuration for session credentials

          device_config: Device configuration for the session. Specify 'mobile' for mobile device
              fingerprints and configurations.

          dimensions: Viewport and browser window dimensions for the session

          extension_ids: Array of extension IDs to install in the session. Use ['all_ext'] to install all
              uploaded extensions.

          headless: Enable headless browser mode (disable Headful mode)

          is_selenium: Enable Selenium mode for the browser session (default is false). Use this when
              you plan to connect to the browser session via Selenium.

          namespace: The namespace the session should be created against. Defaults to "default".

          optimize_bandwidth: Enable bandwidth optimizations. Passing true enables all flags (except
              hosts/patterns). Object allows granular control.

          persist_profile: This flag will persist the user profile for the session.

          profile_id: This flag will set the profile for the session.

          proxy_url: Custom proxy URL for the browser session. Overrides useProxy, disabling
              Steel-provided proxies in favor of your specified proxy. Format:
              http(s)://username:password@hostname:port

          region: The desired region for the session to be started in

          session_context: Session context data to be used in the created session. Sessions will start with
              an empty context by default.

          session_id: Optional custom UUID for the session

          solve_captcha: Enable automatic captcha solving. Default is false.

          stealth_config: Stealth configuration for the session

          api_timeout: Session timeout duration in milliseconds. Default is 300000 (5 minutes).

          use_proxy: Proxy configuration for the session. Can be a boolean or array of proxy
              configurations

          user_agent: Custom user agent string for the browser session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/sessions",
            body=maybe_transform(
                {
                    "block_ads": block_ads,
                    "concurrency": concurrency,
                    "credentials": credentials,
                    "device_config": device_config,
                    "dimensions": dimensions,
                    "extension_ids": extension_ids,
                    "headless": headless,
                    "is_selenium": is_selenium,
                    "namespace": namespace,
                    "optimize_bandwidth": optimize_bandwidth,
                    "persist_profile": persist_profile,
                    "profile_id": profile_id,
                    "proxy_url": proxy_url,
                    "region": region,
                    "session_context": session_context,
                    "session_id": session_id,
                    "solve_captcha": solve_captcha,
                    "stealth_config": stealth_config,
                    "api_timeout": api_timeout or timeout,
                    "use_proxy": use_proxy,
                    "user_agent": user_agent,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypesSession,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypesSession:
        """
        Retrieves details of a specific session by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypesSession,
        )

    def list(
        self,
        *,
        cursor_id: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["live", "released", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSessionsCursor[SessionslistSession]:
        """
        Fetches all active sessions for the current organization.

        Args:
          cursor_id: Cursor ID for pagination

          limit: Number of sessions to return. Default is 50.

          status: Filter sessions by current status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/sessions",
            page=SyncSessionsCursor[SessionslistSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor_id": cursor_id,
                        "limit": limit,
                        "status": status,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            model=SessionslistSession,
        )

    def context(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionContext:
        """
        Fetches the context data of a specific session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/sessions/{id}/context",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionContext,
        )

    def events(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionEventsResponse:
        """
        This endpoint allows you to get the recorded session events in the RRWeb format

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/sessions/{id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionEventsResponse,
        )

    def live_details(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionLiveDetailsResponse:
        """
        Returns the live state of the session, including pages, tabs, and browser state

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/sessions/{id}/live-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLiveDetailsResponse,
        )

    def release(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionReleaseResponse:
        """
        Releases a specific session by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/sessions/{id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionReleaseResponse,
        )

    def release_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionReleaseAllResponse:
        """Releases all active sessions for the current organization."""
        return self._post(
            "/v1/sessions/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionReleaseAllResponse,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def captchas(self) -> AsyncCaptchasResource:
        return AsyncCaptchasResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        block_ads: bool | Omit = omit,
        concurrency: int | Omit = omit,
        credentials: session_create_params.Credentials | Omit = omit,
        device_config: session_create_params.DeviceConfig | Omit = omit,
        dimensions: session_create_params.Dimensions | Omit = omit,
        extension_ids: SequenceNotStr[str] | Omit = omit,
        headless: bool | Omit = omit,
        is_selenium: bool | Omit = omit,
        namespace: str | Omit = omit,
        optimize_bandwidth: session_create_params.OptimizeBandwidth | Omit = omit,
        persist_profile: bool | Omit = omit,
        profile_id: str | Omit = omit,
        proxy_url: str | Omit = omit,
        region: str | Omit = omit,
        session_context: session_create_params.SessionContext | Omit = omit,
        session_id: str | Omit = omit,
        solve_captcha: bool | Omit = omit,
        stealth_config: session_create_params.StealthConfig | Omit = omit,
        api_timeout: int | Omit = omit,
        use_proxy: session_create_params.UseProxy | Omit = omit,
        user_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypesSession:
        """
        Creates a new session with the provided configuration.

        Args:
          block_ads: Block ads in the browser session. Default is false.

          concurrency: Number of sessions to create concurrently (check your plan limit)

          credentials: Configuration for session credentials

          device_config: Device configuration for the session. Specify 'mobile' for mobile device
              fingerprints and configurations.

          dimensions: Viewport and browser window dimensions for the session

          extension_ids: Array of extension IDs to install in the session. Use ['all_ext'] to install all
              uploaded extensions.

          headless: Enable headless browser mode (disable Headful mode)

          is_selenium: Enable Selenium mode for the browser session (default is false). Use this when
              you plan to connect to the browser session via Selenium.

          namespace: The namespace the session should be created against. Defaults to "default".

          optimize_bandwidth: Enable bandwidth optimizations. Passing true enables all flags (except
              hosts/patterns). Object allows granular control.

          persist_profile: This flag will persist the user profile for the session.

          profile_id: This flag will set the profile for the session.

          proxy_url: Custom proxy URL for the browser session. Overrides useProxy, disabling
              Steel-provided proxies in favor of your specified proxy. Format:
              http(s)://username:password@hostname:port

          region: The desired region for the session to be started in

          session_context: Session context data to be used in the created session. Sessions will start with
              an empty context by default.

          session_id: Optional custom UUID for the session

          solve_captcha: Enable automatic captcha solving. Default is false.

          stealth_config: Stealth configuration for the session

          api_timeout: Session timeout duration in milliseconds. Default is 300000 (5 minutes).

          use_proxy: Proxy configuration for the session. Can be a boolean or array of proxy
              configurations

          user_agent: Custom user agent string for the browser session

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/sessions",
            body=await async_maybe_transform(
                {
                    "block_ads": block_ads,
                    "concurrency": concurrency,
                    "credentials": credentials,
                    "device_config": device_config,
                    "dimensions": dimensions,
                    "extension_ids": extension_ids,
                    "headless": headless,
                    "is_selenium": is_selenium,
                    "namespace": namespace,
                    "optimize_bandwidth": optimize_bandwidth,
                    "persist_profile": persist_profile,
                    "profile_id": profile_id,
                    "proxy_url": proxy_url,
                    "region": region,
                    "session_context": session_context,
                    "session_id": session_id,
                    "solve_captcha": solve_captcha,
                    "stealth_config": stealth_config,
                    "api_timeout": api_timeout or timeout,
                    "use_proxy": use_proxy,
                    "user_agent": user_agent,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypesSession,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypesSession:
        """
        Retrieves details of a specific session by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypesSession,
        )

    def list(
        self,
        *,
        cursor_id: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["live", "released", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SessionslistSession, AsyncSessionsCursor[SessionslistSession]]:
        """
        Fetches all active sessions for the current organization.

        Args:
          cursor_id: Cursor ID for pagination

          limit: Number of sessions to return. Default is 50.

          status: Filter sessions by current status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/sessions",
            page=AsyncSessionsCursor[SessionslistSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor_id": cursor_id,
                        "limit": limit,
                        "status": status,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            model=SessionslistSession,
        )

    async def context(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionContext:
        """
        Fetches the context data of a specific session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/sessions/{id}/context",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionContext,
        )

    async def events(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionEventsResponse:
        """
        This endpoint allows you to get the recorded session events in the RRWeb format

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/sessions/{id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionEventsResponse,
        )

    async def live_details(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionLiveDetailsResponse:
        """
        Returns the live state of the session, including pages, tabs, and browser state

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/sessions/{id}/live-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionLiveDetailsResponse,
        )

    async def release(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionReleaseResponse:
        """
        Releases a specific session by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/sessions/{id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionReleaseResponse,
        )

    async def release_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionReleaseAllResponse:
        """Releases all active sessions for the current organization."""
        return await self._post(
            "/v1/sessions/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionReleaseAllResponse,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            sessions.list,
        )
        self.context = to_raw_response_wrapper(
            sessions.context,
        )
        self.events = to_raw_response_wrapper(
            sessions.events,
        )
        self.live_details = to_raw_response_wrapper(
            sessions.live_details,
        )
        self.release = to_raw_response_wrapper(
            sessions.release,
        )
        self.release_all = to_raw_response_wrapper(
            sessions.release_all,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._sessions.files)

    @cached_property
    def captchas(self) -> CaptchasResourceWithRawResponse:
        return CaptchasResourceWithRawResponse(self._sessions.captchas)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sessions.list,
        )
        self.context = async_to_raw_response_wrapper(
            sessions.context,
        )
        self.events = async_to_raw_response_wrapper(
            sessions.events,
        )
        self.live_details = async_to_raw_response_wrapper(
            sessions.live_details,
        )
        self.release = async_to_raw_response_wrapper(
            sessions.release,
        )
        self.release_all = async_to_raw_response_wrapper(
            sessions.release_all,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._sessions.files)

    @cached_property
    def captchas(self) -> AsyncCaptchasResourceWithRawResponse:
        return AsyncCaptchasResourceWithRawResponse(self._sessions.captchas)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sessions.list,
        )
        self.context = to_streamed_response_wrapper(
            sessions.context,
        )
        self.events = to_streamed_response_wrapper(
            sessions.events,
        )
        self.live_details = to_streamed_response_wrapper(
            sessions.live_details,
        )
        self.release = to_streamed_response_wrapper(
            sessions.release,
        )
        self.release_all = to_streamed_response_wrapper(
            sessions.release_all,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._sessions.files)

    @cached_property
    def captchas(self) -> CaptchasResourceWithStreamingResponse:
        return CaptchasResourceWithStreamingResponse(self._sessions.captchas)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sessions.list,
        )
        self.context = async_to_streamed_response_wrapper(
            sessions.context,
        )
        self.events = async_to_streamed_response_wrapper(
            sessions.events,
        )
        self.live_details = async_to_streamed_response_wrapper(
            sessions.live_details,
        )
        self.release = async_to_streamed_response_wrapper(
            sessions.release,
        )
        self.release_all = async_to_streamed_response_wrapper(
            sessions.release_all,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._sessions.files)

    @cached_property
    def captchas(self) -> AsyncCaptchasResourceWithStreamingResponse:
        return AsyncCaptchasResourceWithStreamingResponse(self._sessions.captchas)
