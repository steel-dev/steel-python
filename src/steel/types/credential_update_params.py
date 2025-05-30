# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["CredentialUpdateParams"]


class CredentialUpdateParams(TypedDict, total=False):
    label: str
    """Label for the credential"""

    namespace: str
    """The namespace the credential is stored against. Defaults to "default"."""

    origin: str
    """Website origin the credential is for"""

    value: Dict[str, str]
    """Value for the credential"""
