# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CheckpointList", "Checkpoint"]


class Checkpoint(BaseModel):
    id: str

    computer_id: str = FieldInfo(alias="computerId")

    name: Optional[str] = None

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)

    status: Literal["none", "creating", "ready", "failed", "deleting", "deleted"]

    status_changed_at: datetime = FieldInfo(alias="statusChangedAt")


class CheckpointList(BaseModel):
    checkpoints: List[Checkpoint]
