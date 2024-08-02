# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import context_create_params
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
from ..types.get_context_response import GetContextResponse
from ..types.get_contexts_response import GetContextsResponse
from ..types.create_context_response import CreateContextResponse
from ..types.delete_context_response import DeleteContextResponse

__all__ = ["ContextsResource", "AsyncContextsResource"]


class ContextsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContextsResourceWithRawResponse:
        return ContextsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextsResourceWithStreamingResponse:
        return ContextsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        proxy: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateContextResponse:
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
            body=maybe_transform({"proxy": proxy}, context_create_params.ContextCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateContextResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetContextResponse:
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
            cast_to=GetContextResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetContextsResponse:
        """Retrieve a list of all saved browser contexts"""
        return self._get(
            "/v1/context",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetContextsResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeleteContextResponse:
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
            cast_to=DeleteContextResponse,
        )


class AsyncContextsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContextsResourceWithRawResponse:
        return AsyncContextsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextsResourceWithStreamingResponse:
        return AsyncContextsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        proxy: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateContextResponse:
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
            body=await async_maybe_transform({"proxy": proxy}, context_create_params.ContextCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateContextResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetContextResponse:
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
            cast_to=GetContextResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetContextsResponse:
        """Retrieve a list of all saved browser contexts"""
        return await self._get(
            "/v1/context",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetContextsResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeleteContextResponse:
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
            cast_to=DeleteContextResponse,
        )


class ContextsResourceWithRawResponse:
    def __init__(self, contexts: ContextsResource) -> None:
        self._contexts = contexts

        self.create = to_raw_response_wrapper(
            contexts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contexts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            contexts.list,
        )
        self.delete = to_raw_response_wrapper(
            contexts.delete,
        )


class AsyncContextsResourceWithRawResponse:
    def __init__(self, contexts: AsyncContextsResource) -> None:
        self._contexts = contexts

        self.create = async_to_raw_response_wrapper(
            contexts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contexts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            contexts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contexts.delete,
        )


class ContextsResourceWithStreamingResponse:
    def __init__(self, contexts: ContextsResource) -> None:
        self._contexts = contexts

        self.create = to_streamed_response_wrapper(
            contexts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contexts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            contexts.list,
        )
        self.delete = to_streamed_response_wrapper(
            contexts.delete,
        )


class AsyncContextsResourceWithStreamingResponse:
    def __init__(self, contexts: AsyncContextsResource) -> None:
        self._contexts = contexts

        self.create = async_to_streamed_response_wrapper(
            contexts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contexts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            contexts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contexts.delete,
        )
