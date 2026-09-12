# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CheckpointRestoreParams"]


class CheckpointRestoreParams(TypedDict, total=False):
    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]
    """Pause at the timeout instead of stopping."""

    idle_timeout_seconds: Annotated[int, PropertyInfo(alias="idleTimeoutSeconds")]
    """Pause the restored computer after this many seconds without incoming traffic.

    0 disables idle pausing.
    """

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]
    """
    How long the restored computer may run before it is stopped, or paused when
    autoPause is set.
    """
