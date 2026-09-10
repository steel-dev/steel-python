# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CheckpointRestoreParams"]


class CheckpointRestoreParams(TypedDict, total=False):
    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]
