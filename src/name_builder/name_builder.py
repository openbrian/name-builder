"""The Foo module provides things and functions."""

from random import choice


# pylint: disable=too-few-public-methods
class NameBuilder:
    """The Foo class provides sample methods."""

    @staticmethod
    def generate_name() -> str:
        return choice(NameBuilder.get_colors())

    @staticmethod
    def get_colors() -> list[str]:
        colors: list[str] = ["red", "blue", "chartreuse"]
        return colors
