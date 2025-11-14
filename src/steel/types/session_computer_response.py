# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SessionComputerResponse"]


class SessionComputerResponse(BaseModel):
    base64_image: Optional[str] = None
    """Base64 encoded screenshot if requested"""

    error: Optional[str] = None
    """Error message if action failed"""

    output: Optional[str] = None
    """Output message from the action"""

    system: Optional[str] = None
    """System information"""
