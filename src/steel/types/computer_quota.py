# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ComputerQuota"]


class ComputerQuota(BaseModel):
    checkpoint_count: int = FieldInfo(alias="checkpointCount")

    checkpoint_limit: int = FieldInfo(alias="checkpointLimit")

    computer_count: int = FieldInfo(alias="computerCount")

    computer_limit: int = FieldInfo(alias="computerLimit")

    running_count: int = FieldInfo(alias="runningCount")

    running_limit: int = FieldInfo(alias="runningLimit")
