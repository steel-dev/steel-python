# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ComputerCreateParams"]


class ComputerCreateParams(TypedDict, total=False):
    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]
    """
    Pause at the timeout instead of stopping, so a later resume continues where the
    computer left off. The pause begins about 30 seconds before the deadline.
    """

    disk_mib: Annotated[int, PropertyInfo(alias="diskMib")]
    """Ignored today. Every computer gets the disk its host is configured for."""

    memory_mib: Annotated[int, PropertyInfo(alias="memoryMib")]

    template: str

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]
    """
    How long the computer may run before it is stopped, or paused when autoPause is
    set. A resume starts a fresh window.
    """

    vcpu: int
