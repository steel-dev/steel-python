# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ComputerCreateParams", "NetworkPolicy", "NetworkPolicyCidrs", "NetworkPolicyDomains", "NetworkSecret"]


class ComputerCreateParams(TypedDict, total=False):
    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]
    """
    Pause at the timeout instead of stopping, so a later resume continues where the
    computer left off. The pause begins about 30 seconds before the deadline.
    """

    disk_mib: Annotated[int, PropertyInfo(alias="diskMib")]
    """Ignored today. Every computer gets the disk its host is configured for."""

    env: Dict[str, str]

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]

    idle_timeout_seconds: Annotated[int, PropertyInfo(alias="idleTimeoutSeconds")]
    """
    Pause the computer after this many seconds without incoming traffic, so a later
    resume continues where it left off. 0 disables idle pausing.
    """

    memory_mib: Annotated[int, PropertyInfo(alias="memoryMib")]

    name: str

    network_policy: Annotated[NetworkPolicy, PropertyInfo(alias="networkPolicy")]

    network_secrets: Annotated[Iterable[NetworkSecret], PropertyInfo(alias="networkSecrets")]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    secrets: Dict[str, str]

    template: str

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]
    """
    How long the computer may run before it is stopped, or paused when autoPause is
    set. A resume starts a fresh window.
    """

    vcpu: int


class NetworkPolicyCidrs(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class NetworkPolicyDomains(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class NetworkPolicy(TypedDict, total=False):
    cidrs: NetworkPolicyCidrs

    domains: NetworkPolicyDomains

    internet_access: Annotated[bool, PropertyInfo(alias="internetAccess")]


class NetworkSecret(TypedDict, total=False):
    domain: Required[str]

    header: Required[str]

    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]

    template: Required[str]

    port: int
