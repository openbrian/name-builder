"""Test the Something module. Add more tests here, as needed."""

from random import choice, seed
from unittest import mock
from unittest.mock import Mock, patch

from pytest_randomly import default_seed

from src.name_builder.name_builder import NameBuilder


@patch.object(NameBuilder, "get_colors")
def test_generate_name(mock_get_colors: Mock) -> None:
    """A name_builder test."""
    colors: list[str] = ["red", "blue", "chartreuse"]
    mock_get_colors.return_value = colors
    seed(default_seed)
    expected_color: str = choice(colors)
    assert NameBuilder.generate_name(default_seed) == expected_color


def test_get_colors() -> None:
    mock_open = mock.mock_open(read_data="red\nblue\nchartreuse")
    with patch("builtins.open", mock_open):
        assert "chartreuse" in NameBuilder.get_colors()
