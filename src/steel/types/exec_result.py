# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExecResult"]


class ExecResult(BaseModel):
    exit_code: int = FieldInfo(alias="exitCode")

    output: str

    timed_out: bool = FieldInfo(alias="timedOut")

    truncated: bool
