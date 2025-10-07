# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import credential_list_params, credential_create_params, credential_delete_params, credential_update_params
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
from ..types.credential_list_response import CredentialListResponse
from ..types.credential_create_response import CredentialCreateResponse
from ..types.credential_delete_response import CredentialDeleteResponse
from ..types.credential_update_response import CredentialUpdateResponse

__all__ = ["CredentialsResource", "AsyncCredentialsResource"]


class CredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return CredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return CredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        value: Dict[str, str],
        label: str | Omit = omit,
        namespace: str | Omit = omit,
        origin: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialCreateResponse:
        """
        Encrypts and stores credentials for an origin

        Args:
          value: Value for the credential

          label: Label for the credential

          namespace: The namespace the credential is stored against. Defaults to "default".

          origin: Website origin the credential is for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/credentials",
            body=maybe_transform(
                {
                    "value": value,
                    "label": label,
                    "namespace": namespace,
                    "origin": origin,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialCreateResponse,
        )

    def update(
        self,
        *,
        label: str | Omit = omit,
        namespace: str | Omit = omit,
        origin: str | Omit = omit,
        value: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialUpdateResponse:
        """
        Encrypts and updates credentials for an origin

        Args:
          label: Label for the credential

          namespace: The namespace the credential is stored against. Defaults to "default".

          origin: Website origin the credential is for

          value: Value for the credential

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/credentials",
            body=maybe_transform(
                {
                    "label": label,
                    "namespace": namespace,
                    "origin": origin,
                    "value": value,
                },
                credential_update_params.CredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialUpdateResponse,
        )

    def list(
        self,
        *,
        namespace: str | Omit = omit,
        origin: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialListResponse:
        """
        Fetches all credential metadata for the current organization.

        Args:
          namespace: namespace credential is stored against

          origin: website origin the credential is for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/credentials",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "namespace": namespace,
                        "origin": origin,
                    },
                    credential_list_params.CredentialListParams,
                ),
            ),
            cast_to=CredentialListResponse,
        )

    def delete(
        self,
        *,
        origin: str,
        namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialDeleteResponse:
        """
        Deletes encrypted credentials from the database

        Args:
          origin: Website origin the credential is for

          namespace: The namespace the credential is stored against. Defaults to "default".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/credentials",
            body=maybe_transform(
                {
                    "origin": origin,
                    "namespace": namespace,
                },
                credential_delete_params.CredentialDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialDeleteResponse,
        )


class AsyncCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return AsyncCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        value: Dict[str, str],
        label: str | Omit = omit,
        namespace: str | Omit = omit,
        origin: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialCreateResponse:
        """
        Encrypts and stores credentials for an origin

        Args:
          value: Value for the credential

          label: Label for the credential

          namespace: The namespace the credential is stored against. Defaults to "default".

          origin: Website origin the credential is for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/credentials",
            body=await async_maybe_transform(
                {
                    "value": value,
                    "label": label,
                    "namespace": namespace,
                    "origin": origin,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialCreateResponse,
        )

    async def update(
        self,
        *,
        label: str | Omit = omit,
        namespace: str | Omit = omit,
        origin: str | Omit = omit,
        value: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialUpdateResponse:
        """
        Encrypts and updates credentials for an origin

        Args:
          label: Label for the credential

          namespace: The namespace the credential is stored against. Defaults to "default".

          origin: Website origin the credential is for

          value: Value for the credential

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/credentials",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "namespace": namespace,
                    "origin": origin,
                    "value": value,
                },
                credential_update_params.CredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialUpdateResponse,
        )

    async def list(
        self,
        *,
        namespace: str | Omit = omit,
        origin: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialListResponse:
        """
        Fetches all credential metadata for the current organization.

        Args:
          namespace: namespace credential is stored against

          origin: website origin the credential is for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/credentials",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "namespace": namespace,
                        "origin": origin,
                    },
                    credential_list_params.CredentialListParams,
                ),
            ),
            cast_to=CredentialListResponse,
        )

    async def delete(
        self,
        *,
        origin: str,
        namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialDeleteResponse:
        """
        Deletes encrypted credentials from the database

        Args:
          origin: Website origin the credential is for

          namespace: The namespace the credential is stored against. Defaults to "default".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/credentials",
            body=await async_maybe_transform(
                {
                    "origin": origin,
                    "namespace": namespace,
                },
                credential_delete_params.CredentialDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialDeleteResponse,
        )


class CredentialsResourceWithRawResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.create = to_raw_response_wrapper(
            credentials.create,
        )
        self.update = to_raw_response_wrapper(
            credentials.update,
        )
        self.list = to_raw_response_wrapper(
            credentials.list,
        )
        self.delete = to_raw_response_wrapper(
            credentials.delete,
        )


class AsyncCredentialsResourceWithRawResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.create = async_to_raw_response_wrapper(
            credentials.create,
        )
        self.update = async_to_raw_response_wrapper(
            credentials.update,
        )
        self.list = async_to_raw_response_wrapper(
            credentials.list,
        )
        self.delete = async_to_raw_response_wrapper(
            credentials.delete,
        )


class CredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.create = to_streamed_response_wrapper(
            credentials.create,
        )
        self.update = to_streamed_response_wrapper(
            credentials.update,
        )
        self.list = to_streamed_response_wrapper(
            credentials.list,
        )
        self.delete = to_streamed_response_wrapper(
            credentials.delete,
        )


class AsyncCredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.create = async_to_streamed_response_wrapper(
            credentials.create,
        )
        self.update = async_to_streamed_response_wrapper(
            credentials.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credentials.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            credentials.delete,
        )
