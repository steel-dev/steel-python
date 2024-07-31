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
from .schema import (
    SchemaResource,
    AsyncSchemaResource,
    SchemaResourceWithRawResponse,
    AsyncSchemaResourceWithRawResponse,
    SchemaResourceWithStreamingResponse,
    AsyncSchemaResourceWithStreamingResponse,
)
from .sdk.sdk import SDKResource, AsyncSDKResource
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(SyncAPIResource):
    @cached_property
    def schema(self) -> SchemaResource:
        return SchemaResource(self._client)

    @cached_property
    def sdk(self) -> SDKResource:
        return SDKResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        return APIResourceWithStreamingResponse(self)


class AsyncAPIResource(AsyncAPIResource):
    @cached_property
    def schema(self) -> AsyncSchemaResource:
        return AsyncSchemaResource(self._client)

    @cached_property
    def sdk(self) -> AsyncSDKResource:
        return AsyncSDKResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        return AsyncAPIResourceWithStreamingResponse(self)


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        return SchemaResourceWithRawResponse(self._api.schema)

    @cached_property
    def sdk(self) -> SDKResourceWithRawResponse:
        return SDKResourceWithRawResponse(self._api.sdk)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        return AsyncSchemaResourceWithRawResponse(self._api.schema)

    @cached_property
    def sdk(self) -> AsyncSDKResourceWithRawResponse:
        return AsyncSDKResourceWithRawResponse(self._api.sdk)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        return SchemaResourceWithStreamingResponse(self._api.schema)

    @cached_property
    def sdk(self) -> SDKResourceWithStreamingResponse:
        return SDKResourceWithStreamingResponse(self._api.sdk)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        return AsyncSchemaResourceWithStreamingResponse(self._api.schema)

    @cached_property
    def sdk(self) -> AsyncSDKResourceWithStreamingResponse:
        return AsyncSDKResourceWithStreamingResponse(self._api.sdk)
