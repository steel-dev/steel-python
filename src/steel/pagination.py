# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncCursorPage", "AsyncCursorPage"]

_T = TypeVar("_T")


class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    sessions: List[_T]
    next_cursor: Optional[str] = None
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        sessions = self.sessions
        if not sessions:
            return []
        return sessions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    sessions: List[_T]
    next_cursor: Optional[str] = None
    total_count: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        sessions = self.sessions
        if not sessions:
            return []
        return sessions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
