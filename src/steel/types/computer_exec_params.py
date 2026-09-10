# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ComputerExecParams"]


class ComputerExecParams(TypedDict, total=False):
    argv: SequenceNotStr[str]
    """A program and its arguments, run without a shell."""

    command: str
    """A shell command, run by /bin/sh -c."""

    cwd: str

    env: Dict[str, str]

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]
