# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import overload

import httpx

from ..types import (
    environment_list_params,
    environment_create_params,
    environment_delete_params,
    environment_update_params,
    environment_retrieve_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.environment import Environment
from ..types.environment_list import EnvironmentList

__all__ = ["EnvironmentsResource", "AsyncEnvironmentsResource"]


class EnvironmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return EnvironmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        network_secrets: Iterable[environment_create_params.NetworkSecret] | Omit = omit,
        project_id: str | Omit = omit,
        secrets: Dict[str, environment_create_params.Secrets] | Omit = omit,
        spec: environment_create_params.Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Create an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/environments",
            body=maybe_transform(
                {
                    "name": name,
                    "network_secrets": network_secrets,
                    "project_id": project_id,
                    "secrets": secrets,
                    "spec": spec,
                },
                environment_create_params.EnvironmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Environment,
        )

    def retrieve(
        self,
        id: str,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Get an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/environments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"project_id": project_id}, environment_retrieve_params.EnvironmentRetrieveParams
                ),
            ),
            cast_to=Environment,
        )

    @overload
    def update(
        self,
        id: str,
        *,
        name: str,
        project_id: str | Omit = omit,
        network_secrets: Iterable[environment_update_params.Variant0NetworkSecret] | Omit = omit,
        secrets: Dict[str, environment_update_params.Variant0Secrets] | Omit = omit,
        spec: environment_update_params.Variant0Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Update an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        spec: environment_update_params.Variant1Spec,
        project_id: str | Omit = omit,
        name: str | Omit = omit,
        network_secrets: Iterable[environment_update_params.Variant1NetworkSecret] | Omit = omit,
        secrets: Dict[str, environment_update_params.Variant1Secrets] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Update an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        secrets: Dict[str, environment_update_params.Variant2Secrets],
        project_id: str | Omit = omit,
        name: str | Omit = omit,
        network_secrets: Iterable[environment_update_params.Variant2NetworkSecret] | Omit = omit,
        spec: environment_update_params.Variant2Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Update an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        network_secrets: Iterable[environment_update_params.Variant3NetworkSecret],
        project_id: str | Omit = omit,
        name: str | Omit = omit,
        secrets: Dict[str, environment_update_params.Variant3Secrets] | Omit = omit,
        spec: environment_update_params.Variant3Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Update an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["spec"], ["secrets"], ["network_secrets"])
    def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        project_id: str | Omit = omit,
        network_secrets: Iterable[environment_update_params.Variant0NetworkSecret]
        | Iterable[environment_update_params.Variant1NetworkSecret]
        | Iterable[environment_update_params.Variant2NetworkSecret]
        | Iterable[environment_update_params.Variant3NetworkSecret]
        | Omit = omit,
        secrets: Dict[str, environment_update_params.Variant0Secrets]
        | Dict[str, environment_update_params.Variant1Secrets]
        | Dict[str, environment_update_params.Variant2Secrets]
        | Dict[str, environment_update_params.Variant3Secrets]
        | Omit = omit,
        spec: environment_update_params.Variant0Spec
        | environment_update_params.Variant1Spec
        | environment_update_params.Variant2Spec
        | environment_update_params.Variant3Spec
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/environments/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "network_secrets": network_secrets,
                    "secrets": secrets,
                    "spec": spec,
                },
                environment_update_params.EnvironmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, environment_update_params.EnvironmentUpdateParams),
            ),
            cast_to=Environment,
        )

    def list(
        self,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentList:
        """
        List Environments

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/environments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, environment_list_params.EnvironmentListParams),
            ),
            cast_to=EnvironmentList,
        )

    def delete(
        self,
        id: str,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/environments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, environment_delete_params.EnvironmentDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncEnvironmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return AsyncEnvironmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        network_secrets: Iterable[environment_create_params.NetworkSecret] | Omit = omit,
        project_id: str | Omit = omit,
        secrets: Dict[str, environment_create_params.Secrets] | Omit = omit,
        spec: environment_create_params.Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Create an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/environments",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "network_secrets": network_secrets,
                    "project_id": project_id,
                    "secrets": secrets,
                    "spec": spec,
                },
                environment_create_params.EnvironmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Environment,
        )

    async def retrieve(
        self,
        id: str,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Get an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/environments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, environment_retrieve_params.EnvironmentRetrieveParams
                ),
            ),
            cast_to=Environment,
        )

    @overload
    async def update(
        self,
        id: str,
        *,
        name: str,
        project_id: str | Omit = omit,
        network_secrets: Iterable[environment_update_params.Variant0NetworkSecret] | Omit = omit,
        secrets: Dict[str, environment_update_params.Variant0Secrets] | Omit = omit,
        spec: environment_update_params.Variant0Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Update an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        spec: environment_update_params.Variant1Spec,
        project_id: str | Omit = omit,
        name: str | Omit = omit,
        network_secrets: Iterable[environment_update_params.Variant1NetworkSecret] | Omit = omit,
        secrets: Dict[str, environment_update_params.Variant1Secrets] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Update an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        secrets: Dict[str, environment_update_params.Variant2Secrets],
        project_id: str | Omit = omit,
        name: str | Omit = omit,
        network_secrets: Iterable[environment_update_params.Variant2NetworkSecret] | Omit = omit,
        spec: environment_update_params.Variant2Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Update an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        network_secrets: Iterable[environment_update_params.Variant3NetworkSecret],
        project_id: str | Omit = omit,
        name: str | Omit = omit,
        secrets: Dict[str, environment_update_params.Variant3Secrets] | Omit = omit,
        spec: environment_update_params.Variant3Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        """
        Update an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"], ["spec"], ["secrets"], ["network_secrets"])
    async def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        project_id: str | Omit = omit,
        network_secrets: Iterable[environment_update_params.Variant0NetworkSecret]
        | Iterable[environment_update_params.Variant1NetworkSecret]
        | Iterable[environment_update_params.Variant2NetworkSecret]
        | Iterable[environment_update_params.Variant3NetworkSecret]
        | Omit = omit,
        secrets: Dict[str, environment_update_params.Variant0Secrets]
        | Dict[str, environment_update_params.Variant1Secrets]
        | Dict[str, environment_update_params.Variant2Secrets]
        | Dict[str, environment_update_params.Variant3Secrets]
        | Omit = omit,
        spec: environment_update_params.Variant0Spec
        | environment_update_params.Variant1Spec
        | environment_update_params.Variant2Spec
        | environment_update_params.Variant3Spec
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Environment:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/environments/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "network_secrets": network_secrets,
                    "secrets": secrets,
                    "spec": spec,
                },
                environment_update_params.EnvironmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, environment_update_params.EnvironmentUpdateParams
                ),
            ),
            cast_to=Environment,
        )

    async def list(
        self,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentList:
        """
        List Environments

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/environments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, environment_list_params.EnvironmentListParams
                ),
            ),
            cast_to=EnvironmentList,
        )

    async def delete(
        self,
        id: str,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an Environment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/environments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, environment_delete_params.EnvironmentDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class EnvironmentsResourceWithRawResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.create = to_raw_response_wrapper(
            environments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            environments.retrieve,
        )
        self.update = to_raw_response_wrapper(
            environments.update,
        )
        self.list = to_raw_response_wrapper(
            environments.list,
        )
        self.delete = to_raw_response_wrapper(
            environments.delete,
        )


class AsyncEnvironmentsResourceWithRawResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.create = async_to_raw_response_wrapper(
            environments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            environments.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            environments.update,
        )
        self.list = async_to_raw_response_wrapper(
            environments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            environments.delete,
        )


class EnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.create = to_streamed_response_wrapper(
            environments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            environments.update,
        )
        self.list = to_streamed_response_wrapper(
            environments.list,
        )
        self.delete = to_streamed_response_wrapper(
            environments.delete,
        )


class AsyncEnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.create = async_to_streamed_response_wrapper(
            environments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            environments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            environments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            environments.delete,
        )
