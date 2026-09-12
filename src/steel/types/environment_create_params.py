# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "EnvironmentCreateParams",
    "NetworkSecret",
    "NetworkSecretSecret",
    "NetworkSecretSecretSecretID",
    "NetworkSecretSecretValue",
    "Secrets",
    "SecretsSecretID",
    "SecretsValue",
    "Spec",
    "SpecNetworkPolicy",
    "SpecNetworkPolicyCidrs",
    "SpecNetworkPolicyDomains",
]


class EnvironmentCreateParams(TypedDict, total=False):
    name: Required[str]

    network_secrets: Annotated[Iterable[NetworkSecret], PropertyInfo(alias="networkSecrets")]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    secrets: Dict[str, Secrets]

    spec: Spec


class NetworkSecretSecretSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class NetworkSecretSecretValue(TypedDict, total=False):
    value: Required[str]


NetworkSecretSecret: TypeAlias = Union[NetworkSecretSecretSecretID, NetworkSecretSecretValue]


class NetworkSecret(TypedDict, total=False):
    domain: Required[str]

    header: Required[str]

    secret: Required[NetworkSecretSecret]

    template: Required[str]

    port: int


class SecretsSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class SecretsValue(TypedDict, total=False):
    value: Required[str]


Secrets: TypeAlias = Union[SecretsSecretID, SecretsValue]


class SpecNetworkPolicyCidrs(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class SpecNetworkPolicyDomains(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class SpecNetworkPolicy(TypedDict, total=False):
    cidrs: SpecNetworkPolicyCidrs

    domains: SpecNetworkPolicyDomains

    internet_access: Annotated[bool, PropertyInfo(alias="internetAccess")]


class Spec(TypedDict, total=False):
    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]

    disk_mib: Annotated[int, PropertyInfo(alias="diskMib")]

    env: Dict[str, str]

    memory_mib: Annotated[int, PropertyInfo(alias="memoryMib")]

    name: str

    network_policy: Annotated[SpecNetworkPolicy, PropertyInfo(alias="networkPolicy")]

    template: str

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]

    vcpu: int
