# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CredentialListResponse", "Credential"]


class Credential(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")
    """Date and time the credential was created"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Date and time the credential was last updated"""

    label: Optional[str] = None
    """Label for the credential"""

    namespace: Optional[str] = None
    """The namespace the credential is stored against. Defaults to "default"."""

    origin: Optional[str] = None
    """Website origin the credential is for"""


class CredentialListResponse(BaseModel):
    credentials: List[Credential]
