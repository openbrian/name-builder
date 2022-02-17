"""Test the Something module. Add more tests here, as needed."""

# from pytest_mock import mocker

from hypothesis import given, strategies

from src.name_builder import name_builder


@given(strategies.booleans())
def test_do_something(boolean: bool) -> None:
    """An name_builder test."""
    assert name_builder.NameBuilder.do_something(boolean) is True
