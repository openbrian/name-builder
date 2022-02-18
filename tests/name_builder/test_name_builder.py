"""Test the Something module. Add more tests here, as needed."""

# from pytest_mock import mocker

from src.name_builder import name_builder


def test_geneate_name() -> None:
    """An name_builder test."""
    assert name_builder.NameBuilder.generate_name() == "asdf"
