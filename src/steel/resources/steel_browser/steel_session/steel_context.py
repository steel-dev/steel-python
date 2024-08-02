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
from ....types.steel_browser.steel_session import steel_context_create_context_params
from ....types.steel_browser.steel_session.context import Context
from ....types.steel_browser.steel_session.steel_context_create_context_response import (
    SteelContextCreateContextResponse,
)
from ....types.steel_browser.steel_session.steel_context_delete_context_response import (
    SteelContextDeleteContextResponse,
)

__all__ = ["SteelContextResource", "AsyncSteelContextResource"]


class SteelContextResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SteelContextResourceWithRawResponse:
        return SteelContextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SteelContextResourceWithStreamingResponse:
        return SteelContextResourceWithStreamingResponse(self)

    def create_context(
        self,
        *,
        proxy: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SteelContextCreateContextResponse:
        """
        Create a new browser context with specified settings

        Args:
          proxy: Proxy settings for the context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/context",
            body=maybe_transform({"proxy": proxy}, steel_context_create_context_params.SteelContextCreateContextParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SteelContextCreateContextResponse,
        )

    def delete_context(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SteelContextDeleteContextResponse:
        """
        Delete a specific saved browser context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/context/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SteelContextDeleteContextResponse,
        )

    def get_context_data(
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


class AsyncSteelContextResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSteelContextResourceWithRawResponse:
        return AsyncSteelContextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSteelContextResourceWithStreamingResponse:
        return AsyncSteelContextResourceWithStreamingResponse(self)

    async def create_context(
        self,
        *,
        proxy: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SteelContextCreateContextResponse:
        """
        Create a new browser context with specified settings

        Args:
          proxy: Proxy settings for the context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/context",
            body=await async_maybe_transform(
                {"proxy": proxy}, steel_context_create_context_params.SteelContextCreateContextParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SteelContextCreateContextResponse,
        )

    async def delete_context(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SteelContextDeleteContextResponse:
        """
        Delete a specific saved browser context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/context/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SteelContextDeleteContextResponse,
        )

    async def get_context_data(
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


class SteelContextResourceWithRawResponse:
    def __init__(self, steel_context: SteelContextResource) -> None:
        self._steel_context = steel_context

        self.create_context = to_raw_response_wrapper(
            steel_context.create_context,
        )
        self.delete_context = to_raw_response_wrapper(
            steel_context.delete_context,
        )
        self.get_context_data = to_raw_response_wrapper(
            steel_context.get_context_data,
        )


class AsyncSteelContextResourceWithRawResponse:
    def __init__(self, steel_context: AsyncSteelContextResource) -> None:
        self._steel_context = steel_context

        self.create_context = async_to_raw_response_wrapper(
            steel_context.create_context,
        )
        self.delete_context = async_to_raw_response_wrapper(
            steel_context.delete_context,
        )
        self.get_context_data = async_to_raw_response_wrapper(
            steel_context.get_context_data,
        )


class SteelContextResourceWithStreamingResponse:
    def __init__(self, steel_context: SteelContextResource) -> None:
        self._steel_context = steel_context

        self.create_context = to_streamed_response_wrapper(
            steel_context.create_context,
        )
        self.delete_context = to_streamed_response_wrapper(
            steel_context.delete_context,
        )
        self.get_context_data = to_streamed_response_wrapper(
            steel_context.get_context_data,
        )


class AsyncSteelContextResourceWithStreamingResponse:
    def __init__(self, steel_context: AsyncSteelContextResource) -> None:
        self._steel_context = steel_context

        self.create_context = async_to_streamed_response_wrapper(
            steel_context.create_context,
        )
        self.delete_context = async_to_streamed_response_wrapper(
            steel_context.delete_context,
        )
        self.get_context_data = async_to_streamed_response_wrapper(
            steel_context.get_context_data,
        )
