# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Environment",
    "NetworkSecret",
    "Spec",
    "SpecNetworkPolicy",
    "SpecNetworkPolicyCidrs",
    "SpecNetworkPolicyDomains",
]


class NetworkSecret(BaseModel):
    domain: str

    header: str

    secret_id: str = FieldInfo(alias="secretId")

    template: str

    port: Optional[int] = None


class SpecNetworkPolicyCidrs(BaseModel):
    allow: Optional[List[str]] = None

    deny: Optional[List[str]] = None


class SpecNetworkPolicyDomains(BaseModel):
    allow: Optional[List[str]] = None

    deny: Optional[List[str]] = None


class SpecNetworkPolicy(BaseModel):
    cidrs: Optional[SpecNetworkPolicyCidrs] = None

    domains: Optional[SpecNetworkPolicyDomains] = None

    internet_access: Optional[bool] = FieldInfo(alias="internetAccess", default=None)


class Spec(BaseModel):
    auto_pause: Optional[bool] = FieldInfo(alias="autoPause", default=None)

    disk_mib: Optional[int] = FieldInfo(alias="diskMib", default=None)

    env: Optional[Dict[str, str]] = None

    memory_mib: Optional[int] = FieldInfo(alias="memoryMib", default=None)

    name: Optional[str] = None

    network_policy: Optional[SpecNetworkPolicy] = FieldInfo(alias="networkPolicy", default=None)

    template: Optional[str] = None

    timeout_seconds: Optional[int] = FieldInfo(alias="timeoutSeconds", default=None)

    vcpu: Optional[int] = None


class Environment(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    network_secrets: List[NetworkSecret] = FieldInfo(alias="networkSecrets")

    secrets: Dict[str, str]

    spec: Spec

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int
