# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncSessionsCursor", "AsyncSessionsCursor"]

_T = TypeVar("_T")


@runtime_checkable
class SessionsCursorItem(Protocol):
    id: str


class SyncSessionsCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    sessions: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        sessions = self.sessions
        if not sessions:
            return []
        return sessions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        sessions = self.sessions
        if not sessions:
            return None

        item = cast(Any, sessions[-1])
        if not isinstance(item, SessionsCursorItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"cursorId": item.id})


class AsyncSessionsCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    sessions: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        sessions = self.sessions
        if not sessions:
            return []
        return sessions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        sessions = self.sessions
        if not sessions:
            return None

        item = cast(Any, sessions[-1])
        if not isinstance(item, SessionsCursorItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"cursorId": item.id})
