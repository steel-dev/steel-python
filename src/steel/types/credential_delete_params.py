# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CredentialDeleteParams"]


class CredentialDeleteParams(TypedDict, total=False):
    origin: Required[str]
    """Website origin the credential is for"""

    namespace: str
    """The namespace the credential is stored against. Defaults to "default"."""
