# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import session_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.session import Session
from ..types.release_session_response import ReleaseSessionResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        proxy: str | NotGiven = NOT_GIVEN,
        region: Literal["CA", "US", "FR"] | NotGiven = NOT_GIVEN,
        session_context: object | NotGiven = NOT_GIVEN,
        session_timeout: int | NotGiven = NOT_GIVEN,
        solve_captcha: bool | NotGiven = NOT_GIVEN,
        stealth_mode: bool | NotGiven = NOT_GIVEN,
        user_agent: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Start a new browser session

        Args:
          proxy: Proxy configuration for the browser session

          region: Region for the browser session

          session_context: Custom session context data to be used in the created sessio

          session_timeout: How long after starting should the session timeout (in milliseconds).

          solve_captcha: Flag to enable automatic captcha solving

          stealth_mode: Flag to enable stealth mode for the browser session (default: false)

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
                    "proxy": proxy,
                    "region": region,
                    "session_context": session_context,
                    "session_timeout": session_timeout,
                    "solve_captcha": solve_captcha,
                    "stealth_mode": stealth_mode,
                    "user_agent": user_agent,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def get_context(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get the browser context for a specific session

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
            cast_to=object,
        )

    def get_data(
        self,
        id: str,
        *,
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
        return self._get(
            f"/v1/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseSessionResponse:
        """
        Release and terminate a browser session using its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/sessions/{id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseSessionResponse,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        proxy: str | NotGiven = NOT_GIVEN,
        region: Literal["CA", "US", "FR"] | NotGiven = NOT_GIVEN,
        session_context: object | NotGiven = NOT_GIVEN,
        session_timeout: int | NotGiven = NOT_GIVEN,
        solve_captcha: bool | NotGiven = NOT_GIVEN,
        stealth_mode: bool | NotGiven = NOT_GIVEN,
        user_agent: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Start a new browser session

        Args:
          proxy: Proxy configuration for the browser session

          region: Region for the browser session

          session_context: Custom session context data to be used in the created sessio

          session_timeout: How long after starting should the session timeout (in milliseconds).

          solve_captcha: Flag to enable automatic captcha solving

          stealth_mode: Flag to enable stealth mode for the browser session (default: false)

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
                    "proxy": proxy,
                    "region": region,
                    "session_context": session_context,
                    "session_timeout": session_timeout,
                    "solve_captcha": solve_captcha,
                    "stealth_mode": stealth_mode,
                    "user_agent": user_agent,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def get_context(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get the browser context for a specific session

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
            cast_to=object,
        )

    async def get_data(
        self,
        id: str,
        *,
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
        return await self._get(
            f"/v1/sessions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseSessionResponse:
        """
        Release and terminate a browser session using its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/sessions/{id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseSessionResponse,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.get_context = to_raw_response_wrapper(
            sessions.get_context,
        )
        self.get_data = to_raw_response_wrapper(
            sessions.get_data,
        )
        self.release = to_raw_response_wrapper(
            sessions.release,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.get_context = async_to_raw_response_wrapper(
            sessions.get_context,
        )
        self.get_data = async_to_raw_response_wrapper(
            sessions.get_data,
        )
        self.release = async_to_raw_response_wrapper(
            sessions.release,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.get_context = to_streamed_response_wrapper(
            sessions.get_context,
        )
        self.get_data = to_streamed_response_wrapper(
            sessions.get_data,
        )
        self.release = to_streamed_response_wrapper(
            sessions.release,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.get_context = async_to_streamed_response_wrapper(
            sessions.get_context,
        )
        self.get_data = async_to_streamed_response_wrapper(
            sessions.get_data,
        )
        self.release = async_to_streamed_response_wrapper(
            sessions.release,
        )
