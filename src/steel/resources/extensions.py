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
from ..types.extension_list_response import ExtensionListResponse
from ..types.extension_delete_response import ExtensionDeleteResponse
from ..types.extension_update_response import ExtensionUpdateResponse
from ..types.extension_upload_response import ExtensionUploadResponse
from ..types.extension_delete_all_response import ExtensionDeleteAllResponse

__all__ = ["ExtensionsResource", "AsyncExtensionsResource"]


class ExtensionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return ExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return ExtensionsResourceWithStreamingResponse(self)

    def update(
        self,
        extension_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtensionUpdateResponse:
        """
        Update a Chrome extension (.zip/.crx file) for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extension_id:
            raise ValueError(f"Expected a non-empty value for `extension_id` but received {extension_id!r}")
        return self._put(
            f"/v1/extensions/{extension_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionUpdateResponse,
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
    ) -> ExtensionListResponse:
        """List all extensions for the organization"""
        return self._get(
            "/v1/extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionListResponse,
        )

    def delete(
        self,
        extension_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtensionDeleteResponse:
        """
        Delete an extension by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extension_id:
            raise ValueError(f"Expected a non-empty value for `extension_id` but received {extension_id!r}")
        return self._delete(
            f"/v1/extensions/{extension_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionDeleteResponse,
        )

    def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtensionDeleteAllResponse:
        """Delete all extensions for the organization"""
        return self._delete(
            "/v1/extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionDeleteAllResponse,
        )

    def download(
        self,
        extension_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Download an extension file by extension ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extension_id:
            raise ValueError(f"Expected a non-empty value for `extension_id` but received {extension_id!r}")
        return self._get(
            f"/v1/extensions/{extension_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def upload(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtensionUploadResponse:
        """Upload a Chrome extension (.zip/.crx file) for the organization"""
        return self._post(
            "/v1/extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionUploadResponse,
        )


class AsyncExtensionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return AsyncExtensionsResourceWithStreamingResponse(self)

    async def update(
        self,
        extension_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtensionUpdateResponse:
        """
        Update a Chrome extension (.zip/.crx file) for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extension_id:
            raise ValueError(f"Expected a non-empty value for `extension_id` but received {extension_id!r}")
        return await self._put(
            f"/v1/extensions/{extension_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionUpdateResponse,
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
    ) -> ExtensionListResponse:
        """List all extensions for the organization"""
        return await self._get(
            "/v1/extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionListResponse,
        )

    async def delete(
        self,
        extension_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtensionDeleteResponse:
        """
        Delete an extension by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extension_id:
            raise ValueError(f"Expected a non-empty value for `extension_id` but received {extension_id!r}")
        return await self._delete(
            f"/v1/extensions/{extension_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionDeleteResponse,
        )

    async def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtensionDeleteAllResponse:
        """Delete all extensions for the organization"""
        return await self._delete(
            "/v1/extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionDeleteAllResponse,
        )

    async def download(
        self,
        extension_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Download an extension file by extension ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extension_id:
            raise ValueError(f"Expected a non-empty value for `extension_id` but received {extension_id!r}")
        return await self._get(
            f"/v1/extensions/{extension_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def upload(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtensionUploadResponse:
        """Upload a Chrome extension (.zip/.crx file) for the organization"""
        return await self._post(
            "/v1/extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtensionUploadResponse,
        )


class ExtensionsResourceWithRawResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

        self.update = to_raw_response_wrapper(
            extensions.update,
        )
        self.list = to_raw_response_wrapper(
            extensions.list,
        )
        self.delete = to_raw_response_wrapper(
            extensions.delete,
        )
        self.delete_all = to_raw_response_wrapper(
            extensions.delete_all,
        )
        self.download = to_raw_response_wrapper(
            extensions.download,
        )
        self.upload = to_raw_response_wrapper(
            extensions.upload,
        )


class AsyncExtensionsResourceWithRawResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

        self.update = async_to_raw_response_wrapper(
            extensions.update,
        )
        self.list = async_to_raw_response_wrapper(
            extensions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            extensions.delete,
        )
        self.delete_all = async_to_raw_response_wrapper(
            extensions.delete_all,
        )
        self.download = async_to_raw_response_wrapper(
            extensions.download,
        )
        self.upload = async_to_raw_response_wrapper(
            extensions.upload,
        )


class ExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

        self.update = to_streamed_response_wrapper(
            extensions.update,
        )
        self.list = to_streamed_response_wrapper(
            extensions.list,
        )
        self.delete = to_streamed_response_wrapper(
            extensions.delete,
        )
        self.delete_all = to_streamed_response_wrapper(
            extensions.delete_all,
        )
        self.download = to_streamed_response_wrapper(
            extensions.download,
        )
        self.upload = to_streamed_response_wrapper(
            extensions.upload,
        )


class AsyncExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

        self.update = async_to_streamed_response_wrapper(
            extensions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            extensions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            extensions.delete,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            extensions.delete_all,
        )
        self.download = async_to_streamed_response_wrapper(
            extensions.download,
        )
        self.upload = async_to_streamed_response_wrapper(
            extensions.upload,
        )
