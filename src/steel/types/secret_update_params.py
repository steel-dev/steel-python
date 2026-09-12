# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecretUpdateParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    name: Required[str]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    value: str


class Variant1(TypedDict, total=False):
    value: Required[str]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    name: str


SecretUpdateParams: TypeAlias = Union[Variant0, Variant1]
