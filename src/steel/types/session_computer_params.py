# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "SessionComputerParams",
    "Variant0",
    "Variant1",
    "Variant2",
    "Variant3",
    "Variant4",
    "Variant5",
    "Variant6",
    "Variant7",
    "Variant8",
]


class Variant0(TypedDict, total=False):
    action: Required[Literal["move_mouse"]]

    coordinates: Required[Iterable[float]]
    """X and Y coordinates [x, y]"""

    hold_keys: SequenceNotStr[str]
    """Keys to hold while moving"""

    screenshot: bool
    """Whether to take a screenshot after the action"""


class Variant1(TypedDict, total=False):
    action: Required[Literal["click_mouse"]]

    button: Required[Literal["left", "right", "middle", "back", "forward"]]
    """Mouse button to click"""

    click_type: Literal["down", "up", "click"]
    """Type of click (down, up, or click). Defaults to 'click'"""

    coordinates: Iterable[float]
    """X and Y coordinates [x, y]"""

    hold_keys: SequenceNotStr[str]
    """Keys to hold while clicking"""

    num_clicks: float
    """Number of clicks. Defaults to 1"""

    screenshot: bool
    """Whether to take a screenshot after the action"""


class Variant2(TypedDict, total=False):
    action: Required[Literal["drag_mouse"]]

    path: Required[Iterable[Iterable[float]]]
    """Array of [x, y] coordinate pairs"""

    hold_keys: SequenceNotStr[str]
    """Keys to hold while dragging"""

    screenshot: bool
    """Whether to take a screenshot after the action"""


class Variant3(TypedDict, total=False):
    action: Required[Literal["scroll"]]

    coordinates: Iterable[float]
    """X and Y coordinates [x, y]"""

    delta_x: float
    """Horizontal scroll amount. Defaults to 0"""

    delta_y: float
    """Vertical scroll amount. Defaults to 0"""

    hold_keys: SequenceNotStr[str]
    """Keys to hold while scrolling"""

    screenshot: bool
    """Whether to take a screenshot after the action"""


class Variant4(TypedDict, total=False):
    action: Required[Literal["press_key"]]

    keys: Required[SequenceNotStr[str]]
    """Keys to press"""

    duration: float
    """Duration to hold keys in seconds"""

    screenshot: bool
    """Whether to take a screenshot after the action"""


class Variant5(TypedDict, total=False):
    action: Required[Literal["type_text"]]

    text: Required[str]
    """Text to type"""

    hold_keys: SequenceNotStr[str]
    """Keys to hold while typing"""

    screenshot: bool
    """Whether to take a screenshot after the action"""


class Variant6(TypedDict, total=False):
    action: Required[Literal["wait"]]

    duration: Required[float]
    """Duration to wait in seconds"""

    screenshot: bool
    """Whether to take a screenshot after the action"""


class Variant7(TypedDict, total=False):
    action: Required[Literal["take_screenshot"]]


class Variant8(TypedDict, total=False):
    action: Required[Literal["get_cursor_position"]]


SessionComputerParams: TypeAlias = Union[
    Variant0, Variant1, Variant2, Variant3, Variant4, Variant5, Variant6, Variant7, Variant8
]
