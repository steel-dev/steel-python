# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionComputerParams"]


class SessionComputerParams(TypedDict, total=False):
    body: object
    """Computer action to execute (validation done in controller)"""
