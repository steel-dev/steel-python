# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.context import Context
from ..types.session import Session
from ..types.steel_session_release_session_response import SteelSessionReleaseSessionResponse

__all__ = ["SteelSessionResource", "AsyncSteelSessionResource"]


class SteelSessionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SteelSessionResourceWithRawResponse:
        return SteelSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SteelSessionResourceWithStreamingResponse:
        return SteelSessionResourceWithStreamingResponse(self)

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
    ) -> Context:
        """
        Retrieve details of a specific saved browser context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/context/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Context,
        )

    def get_session_data(
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

    def release_session(
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
    ) -> SteelSessionReleaseSessionResponse:
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
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return self._get(
            f"/v1/sessions/{id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SteelSessionReleaseSessionResponse,
        )


class AsyncSteelSessionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSteelSessionResourceWithRawResponse:
        return AsyncSteelSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSteelSessionResourceWithStreamingResponse:
        return AsyncSteelSessionResourceWithStreamingResponse(self)

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
    ) -> Context:
        """
        Retrieve details of a specific saved browser context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/context/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Context,
        )

    async def get_session_data(
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

    async def release_session(
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
    ) -> SteelSessionReleaseSessionResponse:
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
        extra_headers = {"orgid": orgid, **(extra_headers or {})}
        return await self._get(
            f"/v1/sessions/{id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SteelSessionReleaseSessionResponse,
        )


class SteelSessionResourceWithRawResponse:
    def __init__(self, steel_session: SteelSessionResource) -> None:
        self._steel_session = steel_session

        self.get_context = to_raw_response_wrapper(
            steel_session.get_context,
        )
        self.get_session_data = to_raw_response_wrapper(
            steel_session.get_session_data,
        )
        self.release_session = to_raw_response_wrapper(
            steel_session.release_session,
        )


class AsyncSteelSessionResourceWithRawResponse:
    def __init__(self, steel_session: AsyncSteelSessionResource) -> None:
        self._steel_session = steel_session

        self.get_context = async_to_raw_response_wrapper(
            steel_session.get_context,
        )
        self.get_session_data = async_to_raw_response_wrapper(
            steel_session.get_session_data,
        )
        self.release_session = async_to_raw_response_wrapper(
            steel_session.release_session,
        )


class SteelSessionResourceWithStreamingResponse:
    def __init__(self, steel_session: SteelSessionResource) -> None:
        self._steel_session = steel_session

        self.get_context = to_streamed_response_wrapper(
            steel_session.get_context,
        )
        self.get_session_data = to_streamed_response_wrapper(
            steel_session.get_session_data,
        )
        self.release_session = to_streamed_response_wrapper(
            steel_session.release_session,
        )


class AsyncSteelSessionResourceWithStreamingResponse:
    def __init__(self, steel_session: AsyncSteelSessionResource) -> None:
        self._steel_session = steel_session

        self.get_context = async_to_streamed_response_wrapper(
            steel_session.get_context,
        )
        self.get_session_data = async_to_streamed_response_wrapper(
            steel_session.get_session_data,
        )
        self.release_session = async_to_streamed_response_wrapper(
            steel_session.release_session,
        )
