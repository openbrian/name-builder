"""The Foo module provides things and functions."""

from random import choice, seed
from typing import Optional


# pylint: disable=too-few-public-methods
class NameBuilder:
    """The Foo class provides sample methods."""

    @staticmethod
    def generate_name(the_seed: Optional[int] = None) -> str:
        if seed is not None:
            seed(the_seed)
        return choice(NameBuilder.get_colors())

    @staticmethod
    def get_colors() -> list[str]:
        colors: list[str] = ["red", "blue", "chartreuse"]
        return colors
