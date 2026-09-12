# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    name: Required[str]

    value: Required[str]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
