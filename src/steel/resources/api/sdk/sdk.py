# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .pdf import (
    PdfResource,
    AsyncPdfResource,
    PdfResourceWithRawResponse,
    AsyncPdfResourceWithRawResponse,
    PdfResourceWithStreamingResponse,
    AsyncPdfResourceWithStreamingResponse,
)
from .scrape import (
    ScrapeResource,
    AsyncScrapeResource,
    ScrapeResourceWithRawResponse,
    AsyncScrapeResourceWithRawResponse,
    ScrapeResourceWithStreamingResponse,
    AsyncScrapeResourceWithStreamingResponse,
)
from .context import (
    ContextResource,
    AsyncContextResource,
    ContextResourceWithRawResponse,
    AsyncContextResourceWithRawResponse,
    ContextResourceWithStreamingResponse,
    AsyncContextResourceWithStreamingResponse,
)
from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .screenshot import (
    ScreenshotResource,
    AsyncScreenshotResource,
    ScreenshotResourceWithRawResponse,
    AsyncScreenshotResourceWithRawResponse,
    ScreenshotResourceWithStreamingResponse,
    AsyncScreenshotResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SDKResource", "AsyncSDKResource"]


class SDKResource(SyncAPIResource):
    @cached_property
    def context(self) -> ContextResource:
        return ContextResource(self._client)

    @cached_property
    def pdf(self) -> PdfResource:
        return PdfResource(self._client)

    @cached_property
    def scrape(self) -> ScrapeResource:
        return ScrapeResource(self._client)

    @cached_property
    def screenshot(self) -> ScreenshotResource:
        return ScreenshotResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SDKResourceWithRawResponse:
        return SDKResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SDKResourceWithStreamingResponse:
        return SDKResourceWithStreamingResponse(self)


class AsyncSDKResource(AsyncAPIResource):
    @cached_property
    def context(self) -> AsyncContextResource:
        return AsyncContextResource(self._client)

    @cached_property
    def pdf(self) -> AsyncPdfResource:
        return AsyncPdfResource(self._client)

    @cached_property
    def scrape(self) -> AsyncScrapeResource:
        return AsyncScrapeResource(self._client)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResource:
        return AsyncScreenshotResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSDKResourceWithRawResponse:
        return AsyncSDKResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSDKResourceWithStreamingResponse:
        return AsyncSDKResourceWithStreamingResponse(self)


class SDKResourceWithRawResponse:
    def __init__(self, sdk: SDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def context(self) -> ContextResourceWithRawResponse:
        return ContextResourceWithRawResponse(self._sdk.context)

    @cached_property
    def pdf(self) -> PdfResourceWithRawResponse:
        return PdfResourceWithRawResponse(self._sdk.pdf)

    @cached_property
    def scrape(self) -> ScrapeResourceWithRawResponse:
        return ScrapeResourceWithRawResponse(self._sdk.scrape)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithRawResponse:
        return ScreenshotResourceWithRawResponse(self._sdk.screenshot)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._sdk.sessions)


class AsyncSDKResourceWithRawResponse:
    def __init__(self, sdk: AsyncSDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def context(self) -> AsyncContextResourceWithRawResponse:
        return AsyncContextResourceWithRawResponse(self._sdk.context)

    @cached_property
    def pdf(self) -> AsyncPdfResourceWithRawResponse:
        return AsyncPdfResourceWithRawResponse(self._sdk.pdf)

    @cached_property
    def scrape(self) -> AsyncScrapeResourceWithRawResponse:
        return AsyncScrapeResourceWithRawResponse(self._sdk.scrape)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithRawResponse:
        return AsyncScreenshotResourceWithRawResponse(self._sdk.screenshot)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._sdk.sessions)


class SDKResourceWithStreamingResponse:
    def __init__(self, sdk: SDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def context(self) -> ContextResourceWithStreamingResponse:
        return ContextResourceWithStreamingResponse(self._sdk.context)

    @cached_property
    def pdf(self) -> PdfResourceWithStreamingResponse:
        return PdfResourceWithStreamingResponse(self._sdk.pdf)

    @cached_property
    def scrape(self) -> ScrapeResourceWithStreamingResponse:
        return ScrapeResourceWithStreamingResponse(self._sdk.scrape)

    @cached_property
    def screenshot(self) -> ScreenshotResourceWithStreamingResponse:
        return ScreenshotResourceWithStreamingResponse(self._sdk.screenshot)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._sdk.sessions)


class AsyncSDKResourceWithStreamingResponse:
    def __init__(self, sdk: AsyncSDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def context(self) -> AsyncContextResourceWithStreamingResponse:
        return AsyncContextResourceWithStreamingResponse(self._sdk.context)

    @cached_property
    def pdf(self) -> AsyncPdfResourceWithStreamingResponse:
        return AsyncPdfResourceWithStreamingResponse(self._sdk.pdf)

    @cached_property
    def scrape(self) -> AsyncScrapeResourceWithStreamingResponse:
        return AsyncScrapeResourceWithStreamingResponse(self._sdk.scrape)

    @cached_property
    def screenshot(self) -> AsyncScreenshotResourceWithStreamingResponse:
        return AsyncScreenshotResourceWithStreamingResponse(self._sdk.screenshot)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._sdk.sessions)
