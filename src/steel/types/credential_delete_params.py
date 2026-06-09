# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CredentialDeleteParams"]


class CredentialDeleteParams(TypedDict, total=False):
    origin: Required[str]
    """Website origin the credential is for"""

    namespace: str
    """The namespace the credential is stored against. Defaults to "default"."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Project to delete the credential from."""
