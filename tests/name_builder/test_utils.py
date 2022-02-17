"""Test the utils module in name_builder."""

from src.name_builder.util import rando


def test_rando() -> None:
    assert rando() == 4
