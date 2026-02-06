# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import profile_create_params, profile_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.profile_get_response import ProfileGetResponse
from ..types.profile_list_response import ProfileListResponse
from ..types.profile_create_response import ProfileCreateResponse
from ..types.profile_update_response import ProfileUpdateResponse

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return ProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        user_data_dir: FileTypes,
        dimensions: profile_create_params.Dimensions | Omit = omit,
        proxy_url: str | Omit = omit,
        user_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileCreateResponse:
        """
        Create a new profile

        Args:
          user_data_dir: The user data directory associated with the profile

          dimensions: The dimensions associated with the profile

          proxy_url: The proxy associated with the profile

          user_agent: The user agent associated with the profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "user_data_dir": user_data_dir,
                "dimensions": dimensions,
                "proxy_url": proxy_url,
                "user_agent": user_agent,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["userDataDir"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/profiles",
            body=maybe_transform(body, profile_create_params.ProfileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        user_data_dir: FileTypes,
        dimensions: profile_update_params.Dimensions | Omit = omit,
        proxy_url: str | Omit = omit,
        user_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """
        Update an existing profile

        Args:
          user_data_dir: The user data directory associated with the profile

          dimensions: The dimensions associated with the profile

          proxy_url: The proxy associated with the profile

          user_agent: The user agent associated with the profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        body = deepcopy_minimal(
            {
                "user_data_dir": user_data_dir,
                "dimensions": dimensions,
                "proxy_url": proxy_url,
                "user_agent": user_agent,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["userDataDir"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._patch(
            f"/v1/profiles/{id}",
            body=maybe_transform(body, profile_update_params.ProfileUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
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
    ) -> ProfileListResponse:
        """Retrieve a list of all profiles"""
        return self._get(
            "/v1/profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileListResponse,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileGetResponse:
        """
        Retrieve a profile by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileGetResponse,
        )


class AsyncProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-dev/steel-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-dev/steel-python#with_streaming_response
        """
        return AsyncProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        user_data_dir: FileTypes,
        dimensions: profile_create_params.Dimensions | Omit = omit,
        proxy_url: str | Omit = omit,
        user_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileCreateResponse:
        """
        Create a new profile

        Args:
          user_data_dir: The user data directory associated with the profile

          dimensions: The dimensions associated with the profile

          proxy_url: The proxy associated with the profile

          user_agent: The user agent associated with the profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "user_data_dir": user_data_dir,
                "dimensions": dimensions,
                "proxy_url": proxy_url,
                "user_agent": user_agent,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["userDataDir"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/profiles",
            body=await async_maybe_transform(body, profile_create_params.ProfileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        user_data_dir: FileTypes,
        dimensions: profile_update_params.Dimensions | Omit = omit,
        proxy_url: str | Omit = omit,
        user_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """
        Update an existing profile

        Args:
          user_data_dir: The user data directory associated with the profile

          dimensions: The dimensions associated with the profile

          proxy_url: The proxy associated with the profile

          user_agent: The user agent associated with the profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        body = deepcopy_minimal(
            {
                "user_data_dir": user_data_dir,
                "dimensions": dimensions,
                "proxy_url": proxy_url,
                "user_agent": user_agent,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["userDataDir"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._patch(
            f"/v1/profiles/{id}",
            body=await async_maybe_transform(body, profile_update_params.ProfileUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
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
    ) -> ProfileListResponse:
        """Retrieve a list of all profiles"""
        return await self._get(
            "/v1/profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileListResponse,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileGetResponse:
        """
        Retrieve a profile by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileGetResponse,
        )


class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.create = to_raw_response_wrapper(
            profiles.create,
        )
        self.update = to_raw_response_wrapper(
            profiles.update,
        )
        self.list = to_raw_response_wrapper(
            profiles.list,
        )
        self.get = to_raw_response_wrapper(
            profiles.get,
        )


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = async_to_raw_response_wrapper(
            profiles.create,
        )
        self.update = async_to_raw_response_wrapper(
            profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            profiles.list,
        )
        self.get = async_to_raw_response_wrapper(
            profiles.get,
        )


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.create = to_streamed_response_wrapper(
            profiles.create,
        )
        self.update = to_streamed_response_wrapper(
            profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            profiles.list,
        )
        self.get = to_streamed_response_wrapper(
            profiles.get,
        )


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = async_to_streamed_response_wrapper(
            profiles.create,
        )
        self.update = async_to_streamed_response_wrapper(
            profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            profiles.list,
        )
        self.get = async_to_streamed_response_wrapper(
            profiles.get,
        )
