"""The Foo module provides things and functions."""

from csv import reader
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
        colors_file = "src/name_builder/data/colors.csv"
        with open(colors_file, encoding="utf-8") as file:
            colors = reader(file)
            return [color[0] for color in colors]
