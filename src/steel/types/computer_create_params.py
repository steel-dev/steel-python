# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ComputerCreateParams"]


class ComputerCreateParams(TypedDict, total=False):
    template: Required[str]

    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]

    disk_mib: Annotated[int, PropertyInfo(alias="diskMib")]

    memory_mib: Annotated[int, PropertyInfo(alias="memoryMib")]

    region: Literal[
        "us-east", "us-west", "us-central", "eu-west", "eu-central", "ap-northeast", "ap-southeast", "sa-east"
    ]

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]

    vcpu: int
