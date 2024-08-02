# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TopLevelListSessionsParams"]


class TopLevelListSessionsParams(TypedDict, total=False):
    orgid: Required[str]

    live_only: bool
    """Flag to retrieve only live sessions (default: true)"""
