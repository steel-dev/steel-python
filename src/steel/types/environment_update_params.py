# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "EnvironmentUpdateParams",
    "Variant0",
    "Variant0NetworkSecret",
    "Variant0NetworkSecretSecret",
    "Variant0NetworkSecretSecretSecretID",
    "Variant0NetworkSecretSecretValue",
    "Variant0Secrets",
    "Variant0SecretsSecretID",
    "Variant0SecretsValue",
    "Variant0Spec",
    "Variant0SpecNetworkPolicy",
    "Variant0SpecNetworkPolicyCidrs",
    "Variant0SpecNetworkPolicyDomains",
    "Variant1",
    "Variant1Spec",
    "Variant1SpecNetworkPolicy",
    "Variant1SpecNetworkPolicyCidrs",
    "Variant1SpecNetworkPolicyDomains",
    "Variant1NetworkSecret",
    "Variant1NetworkSecretSecret",
    "Variant1NetworkSecretSecretSecretID",
    "Variant1NetworkSecretSecretValue",
    "Variant1Secrets",
    "Variant1SecretsSecretID",
    "Variant1SecretsValue",
    "Variant2",
    "Variant2Secrets",
    "Variant2SecretsSecretID",
    "Variant2SecretsValue",
    "Variant2NetworkSecret",
    "Variant2NetworkSecretSecret",
    "Variant2NetworkSecretSecretSecretID",
    "Variant2NetworkSecretSecretValue",
    "Variant2Spec",
    "Variant2SpecNetworkPolicy",
    "Variant2SpecNetworkPolicyCidrs",
    "Variant2SpecNetworkPolicyDomains",
    "Variant3",
    "Variant3NetworkSecret",
    "Variant3NetworkSecretSecret",
    "Variant3NetworkSecretSecretSecretID",
    "Variant3NetworkSecretSecretValue",
    "Variant3Secrets",
    "Variant3SecretsSecretID",
    "Variant3SecretsValue",
    "Variant3Spec",
    "Variant3SpecNetworkPolicy",
    "Variant3SpecNetworkPolicyCidrs",
    "Variant3SpecNetworkPolicyDomains",
]


class Variant0(TypedDict, total=False):
    name: Required[str]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    network_secrets: Annotated[Iterable[Variant0NetworkSecret], PropertyInfo(alias="networkSecrets")]

    secrets: Dict[str, Variant0Secrets]

    spec: Variant0Spec


class Variant0NetworkSecretSecretSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class Variant0NetworkSecretSecretValue(TypedDict, total=False):
    value: Required[str]


Variant0NetworkSecretSecret: TypeAlias = Union[Variant0NetworkSecretSecretSecretID, Variant0NetworkSecretSecretValue]


class Variant0NetworkSecret(TypedDict, total=False):
    domain: Required[str]

    header: Required[str]

    secret: Required[Variant0NetworkSecretSecret]

    template: Required[str]

    port: int


class Variant0SecretsSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class Variant0SecretsValue(TypedDict, total=False):
    value: Required[str]


Variant0Secrets: TypeAlias = Union[Variant0SecretsSecretID, Variant0SecretsValue, Optional[str]]


class Variant0SpecNetworkPolicyCidrs(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class Variant0SpecNetworkPolicyDomains(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class Variant0SpecNetworkPolicy(TypedDict, total=False):
    cidrs: Variant0SpecNetworkPolicyCidrs

    domains: Variant0SpecNetworkPolicyDomains

    internet_access: Annotated[bool, PropertyInfo(alias="internetAccess")]


class Variant0Spec(TypedDict, total=False):
    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]

    disk_mib: Annotated[int, PropertyInfo(alias="diskMib")]

    env: Dict[str, str]

    memory_mib: Annotated[int, PropertyInfo(alias="memoryMib")]

    name: str

    network_policy: Annotated[Variant0SpecNetworkPolicy, PropertyInfo(alias="networkPolicy")]

    template: str

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]

    vcpu: int


class Variant1(TypedDict, total=False):
    spec: Required[Variant1Spec]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    name: str

    network_secrets: Annotated[Iterable[Variant1NetworkSecret], PropertyInfo(alias="networkSecrets")]

    secrets: Dict[str, Variant1Secrets]


class Variant1SpecNetworkPolicyCidrs(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class Variant1SpecNetworkPolicyDomains(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class Variant1SpecNetworkPolicy(TypedDict, total=False):
    cidrs: Variant1SpecNetworkPolicyCidrs

    domains: Variant1SpecNetworkPolicyDomains

    internet_access: Annotated[bool, PropertyInfo(alias="internetAccess")]


class Variant1Spec(TypedDict, total=False):
    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]

    disk_mib: Annotated[int, PropertyInfo(alias="diskMib")]

    env: Dict[str, str]

    memory_mib: Annotated[int, PropertyInfo(alias="memoryMib")]

    name: str

    network_policy: Annotated[Variant1SpecNetworkPolicy, PropertyInfo(alias="networkPolicy")]

    template: str

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]

    vcpu: int


class Variant1NetworkSecretSecretSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class Variant1NetworkSecretSecretValue(TypedDict, total=False):
    value: Required[str]


Variant1NetworkSecretSecret: TypeAlias = Union[Variant1NetworkSecretSecretSecretID, Variant1NetworkSecretSecretValue]


class Variant1NetworkSecret(TypedDict, total=False):
    domain: Required[str]

    header: Required[str]

    secret: Required[Variant1NetworkSecretSecret]

    template: Required[str]

    port: int


class Variant1SecretsSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class Variant1SecretsValue(TypedDict, total=False):
    value: Required[str]


Variant1Secrets: TypeAlias = Union[Variant1SecretsSecretID, Variant1SecretsValue, Optional[str]]


class Variant2(TypedDict, total=False):
    secrets: Required[Dict[str, Variant2Secrets]]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    name: str

    network_secrets: Annotated[Iterable[Variant2NetworkSecret], PropertyInfo(alias="networkSecrets")]

    spec: Variant2Spec


class Variant2SecretsSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class Variant2SecretsValue(TypedDict, total=False):
    value: Required[str]


Variant2Secrets: TypeAlias = Union[Variant2SecretsSecretID, Variant2SecretsValue, Optional[str]]


class Variant2NetworkSecretSecretSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class Variant2NetworkSecretSecretValue(TypedDict, total=False):
    value: Required[str]


Variant2NetworkSecretSecret: TypeAlias = Union[Variant2NetworkSecretSecretSecretID, Variant2NetworkSecretSecretValue]


class Variant2NetworkSecret(TypedDict, total=False):
    domain: Required[str]

    header: Required[str]

    secret: Required[Variant2NetworkSecretSecret]

    template: Required[str]

    port: int


class Variant2SpecNetworkPolicyCidrs(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class Variant2SpecNetworkPolicyDomains(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class Variant2SpecNetworkPolicy(TypedDict, total=False):
    cidrs: Variant2SpecNetworkPolicyCidrs

    domains: Variant2SpecNetworkPolicyDomains

    internet_access: Annotated[bool, PropertyInfo(alias="internetAccess")]


class Variant2Spec(TypedDict, total=False):
    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]

    disk_mib: Annotated[int, PropertyInfo(alias="diskMib")]

    env: Dict[str, str]

    memory_mib: Annotated[int, PropertyInfo(alias="memoryMib")]

    name: str

    network_policy: Annotated[Variant2SpecNetworkPolicy, PropertyInfo(alias="networkPolicy")]

    template: str

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]

    vcpu: int


class Variant3(TypedDict, total=False):
    network_secrets: Required[Annotated[Iterable[Variant3NetworkSecret], PropertyInfo(alias="networkSecrets")]]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    name: str

    secrets: Dict[str, Variant3Secrets]

    spec: Variant3Spec


class Variant3NetworkSecretSecretSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class Variant3NetworkSecretSecretValue(TypedDict, total=False):
    value: Required[str]


Variant3NetworkSecretSecret: TypeAlias = Union[Variant3NetworkSecretSecretSecretID, Variant3NetworkSecretSecretValue]


class Variant3NetworkSecret(TypedDict, total=False):
    domain: Required[str]

    header: Required[str]

    secret: Required[Variant3NetworkSecretSecret]

    template: Required[str]

    port: int


class Variant3SecretsSecretID(TypedDict, total=False):
    secret_id: Required[Annotated[str, PropertyInfo(alias="secretId")]]


class Variant3SecretsValue(TypedDict, total=False):
    value: Required[str]


Variant3Secrets: TypeAlias = Union[Variant3SecretsSecretID, Variant3SecretsValue, Optional[str]]


class Variant3SpecNetworkPolicyCidrs(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class Variant3SpecNetworkPolicyDomains(TypedDict, total=False):
    allow: SequenceNotStr[str]

    deny: SequenceNotStr[str]


class Variant3SpecNetworkPolicy(TypedDict, total=False):
    cidrs: Variant3SpecNetworkPolicyCidrs

    domains: Variant3SpecNetworkPolicyDomains

    internet_access: Annotated[bool, PropertyInfo(alias="internetAccess")]


class Variant3Spec(TypedDict, total=False):
    auto_pause: Annotated[bool, PropertyInfo(alias="autoPause")]

    disk_mib: Annotated[int, PropertyInfo(alias="diskMib")]

    env: Dict[str, str]

    memory_mib: Annotated[int, PropertyInfo(alias="memoryMib")]

    name: str

    network_policy: Annotated[Variant3SpecNetworkPolicy, PropertyInfo(alias="networkPolicy")]

    template: str

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]

    vcpu: int


EnvironmentUpdateParams: TypeAlias = Union[Variant0, Variant1, Variant2, Variant3]
