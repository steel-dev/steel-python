# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from steel import Steel, AsyncSteel
from steel.types import (
    Session as TypesSession,
    SessionContext,
    SessionEventsResponse,
    SessionReleaseResponse,
    SessionReleaseAllResponse,
    SessionLiveDetailsResponse,
)
from tests.utils import assert_matches_type
from steel._utils import parse_datetime
from steel.pagination import SyncSessionsCursor, AsyncSessionsCursor
from steel.types.sessionslist import Session as SessionslistSession

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Steel) -> None:
        session = client.sessions.create()
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Steel) -> None:
        session = client.sessions.create(
            block_ads=True,
            concurrency=0,
            credentials={
                "auto_submit": True,
                "blur_fields": True,
                "exact_origin": True,
            },
            device_config={"device": "desktop"},
            dimensions={
                "height": 0,
                "width": 0,
            },
            extension_ids=["string"],
            headless=True,
            is_selenium=True,
            namespace="namespace",
            optimize_bandwidth=True,
            persist_profile=True,
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            proxy_url="https://example.com",
            region="region",
            session_context={
                "cookies": [
                    {
                        "name": "name",
                        "value": "value",
                        "domain": "domain",
                        "expires": 0,
                        "http_only": True,
                        "partition_key": {
                            "has_cross_site_ancestor": True,
                            "top_level_site": "topLevelSite",
                        },
                        "path": "path",
                        "priority": "Low",
                        "same_party": True,
                        "same_site": "Strict",
                        "secure": True,
                        "session": True,
                        "size": 0,
                        "source_port": 0,
                        "source_scheme": "Unset",
                        "url": "url",
                    }
                ],
                "indexed_db": {
                    "foo": [
                        {
                            "id": 0,
                            "data": [
                                {
                                    "id": 0,
                                    "name": "name",
                                    "records": [
                                        {
                                            "blob_files": [
                                                {
                                                    "blob_number": 0,
                                                    "mime_type": "mimeType",
                                                    "size": 0,
                                                    "filename": "filename",
                                                    "last_modified": parse_datetime("2019-12-27T18:11:19.117Z"),
                                                    "path": "path",
                                                }
                                            ],
                                            "key": {},
                                            "value": {},
                                        }
                                    ],
                                }
                            ],
                            "name": "name",
                        }
                    ]
                },
                "local_storage": {"foo": {"foo": "string"}},
                "session_storage": {"foo": {"foo": "string"}},
            },
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            solve_captcha=True,
            stealth_config={
                "humanize_interactions": True,
                "skip_fingerprint_injection": True,
            },
            api_timeout=0,
            use_proxy=True,
            user_agent="userAgent",
        )
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Steel) -> None:
        response = client.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Steel) -> None:
        with client.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(TypesSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Steel) -> None:
        session = client.sessions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Steel) -> None:
        response = client.sessions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Steel) -> None:
        with client.sessions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(TypesSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Steel) -> None:
        session = client.sessions.list()
        assert_matches_type(SyncSessionsCursor[SessionslistSession], session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Steel) -> None:
        session = client.sessions.list(
            cursor_id="cursorId",
            limit=0,
            status="live",
        )
        assert_matches_type(SyncSessionsCursor[SessionslistSession], session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Steel) -> None:
        response = client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SyncSessionsCursor[SessionslistSession], session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Steel) -> None:
        with client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SyncSessionsCursor[SessionslistSession], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_context(self, client: Steel) -> None:
        session = client.sessions.context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SessionContext, session, path=["response"])

    @parametrize
    def test_raw_response_context(self, client: Steel) -> None:
        response = client.sessions.with_raw_response.context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionContext, session, path=["response"])

    @parametrize
    def test_streaming_response_context(self, client: Steel) -> None:
        with client.sessions.with_streaming_response.context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionContext, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_context(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.with_raw_response.context(
                "",
            )

    @parametrize
    def test_method_events(self, client: Steel) -> None:
        session = client.sessions.events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SessionEventsResponse, session, path=["response"])

    @parametrize
    def test_raw_response_events(self, client: Steel) -> None:
        response = client.sessions.with_raw_response.events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionEventsResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_events(self, client: Steel) -> None:
        with client.sessions.with_streaming_response.events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionEventsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_events(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.with_raw_response.events(
                "",
            )

    @parametrize
    def test_method_live_details(self, client: Steel) -> None:
        session = client.sessions.live_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SessionLiveDetailsResponse, session, path=["response"])

    @parametrize
    def test_raw_response_live_details(self, client: Steel) -> None:
        response = client.sessions.with_raw_response.live_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionLiveDetailsResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_live_details(self, client: Steel) -> None:
        with client.sessions.with_streaming_response.live_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionLiveDetailsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_live_details(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.with_raw_response.live_details(
                "",
            )

    @parametrize
    def test_method_release(self, client: Steel) -> None:
        session = client.sessions.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SessionReleaseResponse, session, path=["response"])

    @parametrize
    def test_raw_response_release(self, client: Steel) -> None:
        response = client.sessions.with_raw_response.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionReleaseResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_release(self, client: Steel) -> None:
        with client.sessions.with_streaming_response.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionReleaseResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_release(self, client: Steel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sessions.with_raw_response.release(
                "",
            )

    @parametrize
    def test_method_release_all(self, client: Steel) -> None:
        session = client.sessions.release_all()
        assert_matches_type(SessionReleaseAllResponse, session, path=["response"])

    @parametrize
    def test_raw_response_release_all(self, client: Steel) -> None:
        response = client.sessions.with_raw_response.release_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionReleaseAllResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_release_all(self, client: Steel) -> None:
        with client.sessions.with_streaming_response.release_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionReleaseAllResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.create()
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.create(
            block_ads=True,
            concurrency=0,
            credentials={
                "auto_submit": True,
                "blur_fields": True,
                "exact_origin": True,
            },
            device_config={"device": "desktop"},
            dimensions={
                "height": 0,
                "width": 0,
            },
            extension_ids=["string"],
            headless=True,
            is_selenium=True,
            namespace="namespace",
            optimize_bandwidth=True,
            persist_profile=True,
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            proxy_url="https://example.com",
            region="region",
            session_context={
                "cookies": [
                    {
                        "name": "name",
                        "value": "value",
                        "domain": "domain",
                        "expires": 0,
                        "http_only": True,
                        "partition_key": {
                            "has_cross_site_ancestor": True,
                            "top_level_site": "topLevelSite",
                        },
                        "path": "path",
                        "priority": "Low",
                        "same_party": True,
                        "same_site": "Strict",
                        "secure": True,
                        "session": True,
                        "size": 0,
                        "source_port": 0,
                        "source_scheme": "Unset",
                        "url": "url",
                    }
                ],
                "indexed_db": {
                    "foo": [
                        {
                            "id": 0,
                            "data": [
                                {
                                    "id": 0,
                                    "name": "name",
                                    "records": [
                                        {
                                            "blob_files": [
                                                {
                                                    "blob_number": 0,
                                                    "mime_type": "mimeType",
                                                    "size": 0,
                                                    "filename": "filename",
                                                    "last_modified": parse_datetime("2019-12-27T18:11:19.117Z"),
                                                    "path": "path",
                                                }
                                            ],
                                            "key": {},
                                            "value": {},
                                        }
                                    ],
                                }
                            ],
                            "name": "name",
                        }
                    ]
                },
                "local_storage": {"foo": {"foo": "string"}},
                "session_storage": {"foo": {"foo": "string"}},
            },
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            solve_captcha=True,
            stealth_config={
                "humanize_interactions": True,
                "skip_fingerprint_injection": True,
            },
            api_timeout=0,
            use_proxy=True,
            user_agent="userAgent",
        )
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(TypesSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(TypesSession, session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(TypesSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.list()
        assert_matches_type(AsyncSessionsCursor[SessionslistSession], session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.list(
            cursor_id="cursorId",
            limit=0,
            status="live",
        )
        assert_matches_type(AsyncSessionsCursor[SessionslistSession], session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AsyncSessionsCursor[SessionslistSession], session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AsyncSessionsCursor[SessionslistSession], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_context(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SessionContext, session, path=["response"])

    @parametrize
    async def test_raw_response_context(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.with_raw_response.context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionContext, session, path=["response"])

    @parametrize
    async def test_streaming_response_context(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.with_streaming_response.context(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionContext, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_context(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.with_raw_response.context(
                "",
            )

    @parametrize
    async def test_method_events(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SessionEventsResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_events(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.with_raw_response.events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionEventsResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.with_streaming_response.events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionEventsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_events(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.with_raw_response.events(
                "",
            )

    @parametrize
    async def test_method_live_details(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.live_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SessionLiveDetailsResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_live_details(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.with_raw_response.live_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionLiveDetailsResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_live_details(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.with_streaming_response.live_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionLiveDetailsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_live_details(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.with_raw_response.live_details(
                "",
            )

    @parametrize
    async def test_method_release(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SessionReleaseResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_release(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.with_raw_response.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionReleaseResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.with_streaming_response.release(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionReleaseResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_release(self, async_client: AsyncSteel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sessions.with_raw_response.release(
                "",
            )

    @parametrize
    async def test_method_release_all(self, async_client: AsyncSteel) -> None:
        session = await async_client.sessions.release_all()
        assert_matches_type(SessionReleaseAllResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_release_all(self, async_client: AsyncSteel) -> None:
        response = await async_client.sessions.with_raw_response.release_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionReleaseAllResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_release_all(self, async_client: AsyncSteel) -> None:
        async with async_client.sessions.with_streaming_response.release_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionReleaseAllResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True
