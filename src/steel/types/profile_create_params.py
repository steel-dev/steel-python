# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProfileCreateParams", "Dimensions"]


class ProfileCreateParams(TypedDict, total=False):
    dimensions: Dimensions
    """The dimensions associated with the profile"""

    proxy_url: Annotated[str, PropertyInfo(alias="proxyUrl")]
    """The proxy associated with the profile"""

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]
    """The user agent associated with the profile"""

    user_data_dir: Annotated[object, PropertyInfo(alias="userDataDir")]
    """The user data directory associated with the profile"""


class Dimensions(TypedDict, total=False):
    height: Required[float]

    width: Required[float]
