# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CredentialCreateParams"]


class CredentialCreateParams(TypedDict, total=False):
    value: Required[Dict[str, str]]
    """Value for the credential"""

    label: str
    """Label for the credential"""

    namespace: str
    """The namespace the credential is stored against. Defaults to "default"."""

    origin: str
    """Website origin the credential is for"""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Project to store the credential in."""
