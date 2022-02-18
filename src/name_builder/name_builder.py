"""The Foo module provides things and functions."""


# pylint: disable=too-few-public-methods
class NameBuilder:
    """The Foo class provides sample methods."""

    @staticmethod
    def generate_name() -> str:
        return NameBuilder.get_colors()[0]

    @staticmethod
    def get_colors() -> list[str]:
        colors: list[str] = ["red", "blue", "chartreuse"]
        return colors
