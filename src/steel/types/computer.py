# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Computer"]


class Computer(BaseModel):
    id: str

    auto_pause: bool = FieldInfo(alias="autoPause")

    checkpoint_id: Optional[str] = FieldInfo(alias="checkpointId", default=None)

    disk_mib: int = FieldInfo(alias="diskMib")

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)

    idle_timeout_seconds: int = FieldInfo(alias="idleTimeoutSeconds")

    memory_mib: int = FieldInfo(alias="memoryMib")

    project_id: str = FieldInfo(alias="projectId")

    status: Literal[
        "none", "creating", "running", "pausing", "paused", "waking", "stopped", "failed", "deleting", "deleted"
    ]

    status_changed_at: datetime = FieldInfo(alias="statusChangedAt")

    template: Optional[str] = None

    timeout_seconds: Optional[int] = FieldInfo(alias="timeoutSeconds", default=None)

    vcpu: int
