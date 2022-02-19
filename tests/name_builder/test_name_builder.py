"""Test the Something module. Add more tests here, as needed."""

from unittest.mock import Mock, patch

from src.name_builder.name_builder import NameBuilder


@patch.object(NameBuilder, "get_colors")
def test_generate_name(mock_get_colors: Mock) -> None:
    """A name_builder test."""
    colors: list[str] = ["red", "blue", "chartreuse"]
    mock_get_colors.return_value = colors
    assert NameBuilder.generate_name() == "chartreuse"


def test_get_colors() -> None:
    assert "chartreuse" in NameBuilder.get_colors()
