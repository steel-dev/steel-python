# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import extension_update_params, extension_upload_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
        file: object | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionUpdateResponse:
        """
        Update a Chrome extension (.zip/.crx file or Chrome Web Store URL) for the
        organization

        Args:
          file: Extension .zip/.crx file

          url: Extension URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extension_id:
            raise ValueError(f"Expected a non-empty value for `extension_id` but received {extension_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/v1/extensions/{extension_id}",
            body=maybe_transform(
                {
                    "file": file,
                    "url": url,
                },
                extension_update_params.ExtensionUpdateParams,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        file: object | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionUploadResponse:
        """
        Upload a Chrome extension (.zip/.crx file or Chrome Web Store URL) for the
        organization

        Args:
          file: Extension .zip/.crx file

          url: Extension URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/extensions",
            body=maybe_transform(
                {
                    "file": file,
                    "url": url,
                },
                extension_upload_params.ExtensionUploadParams,
            ),
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
        file: object | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionUpdateResponse:
        """
        Update a Chrome extension (.zip/.crx file or Chrome Web Store URL) for the
        organization

        Args:
          file: Extension .zip/.crx file

          url: Extension URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extension_id:
            raise ValueError(f"Expected a non-empty value for `extension_id` but received {extension_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/v1/extensions/{extension_id}",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "url": url,
                },
                extension_update_params.ExtensionUpdateParams,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        file: object | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionUploadResponse:
        """
        Upload a Chrome extension (.zip/.crx file or Chrome Web Store URL) for the
        organization

        Args:
          file: Extension .zip/.crx file

          url: Extension URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/extensions",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "url": url,
                },
                extension_upload_params.ExtensionUploadParams,
            ),
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
