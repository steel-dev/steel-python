# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ComputerTransitions", "Transition"]


class Transition(BaseModel):
    at: datetime

    detail: object

    from_: Literal[
        "none", "creating", "running", "pausing", "paused", "waking", "stopped", "failed", "deleting", "deleted"
    ] = FieldInfo(alias="from")

    seq: int

    source: Literal["intent", "report", "feed", "sweep"]

    to: Literal[
        "none", "creating", "running", "pausing", "paused", "waking", "stopped", "failed", "deleting", "deleted"
    ]


class ComputerTransitions(BaseModel):
    transitions: List[Transition]
