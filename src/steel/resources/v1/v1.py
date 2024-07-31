# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sdk import (
    SDKResource,
    AsyncSDKResource,
    SDKResourceWithRawResponse,
    AsyncSDKResourceWithRawResponse,
    SDKResourceWithStreamingResponse,
    AsyncSDKResourceWithStreamingResponse,
)
from .sdk.sdk import SDKResource, AsyncSDKResource
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def sdk(self) -> SDKResource:
        return SDKResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def sdk(self) -> AsyncSDKResource:
        return AsyncSDKResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def sdk(self) -> SDKResourceWithRawResponse:
        return SDKResourceWithRawResponse(self._v1.sdk)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def sdk(self) -> AsyncSDKResourceWithRawResponse:
        return AsyncSDKResourceWithRawResponse(self._v1.sdk)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def sdk(self) -> SDKResourceWithStreamingResponse:
        return SDKResourceWithStreamingResponse(self._v1.sdk)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def sdk(self) -> AsyncSDKResourceWithStreamingResponse:
        return AsyncSDKResourceWithStreamingResponse(self._v1.sdk)
