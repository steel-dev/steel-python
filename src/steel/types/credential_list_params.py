# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CredentialListParams"]


class CredentialListParams(TypedDict, total=False):
    namespace: str
    """namespace credential is stored against"""

    origin: str
    """website origin the credential is for"""
