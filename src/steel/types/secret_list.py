# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SecretList", "Secret"]


class Secret(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    source: Literal["steel"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int


class SecretList(BaseModel):
    secrets: List[Secret]
