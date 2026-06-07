# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ProfileUpdateParams", "Dimensions"]


class ProfileUpdateParams(TypedDict, total=False):
    user_data_dir: Required[Annotated[FileTypes, PropertyInfo(alias="userDataDir")]]
    """The user data directory associated with the profile"""

    query_project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Project to query profiles from"""

    dimensions: Dimensions
    """The dimensions associated with the profile"""

    body_project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Project to create the profile in"""

    proxy_url: Annotated[str, PropertyInfo(alias="proxyUrl")]
    """The proxy associated with the profile"""

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]
    """The user agent associated with the profile"""


class Dimensions(TypedDict, total=False):
    """The dimensions associated with the profile"""

    height: Required[float]

    width: Required[float]
