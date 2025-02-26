# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionContext"]


class SessionContext(BaseModel):
    cookies: List[Dict[str, object]]
    """List of cookies associated with the session"""

    local_storage: Dict[str, object] = FieldInfo(alias="localStorage")
    """Local storage data associated with the session"""
