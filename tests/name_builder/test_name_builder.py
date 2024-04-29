"""Test the Something module. Add more tests here, as needed."""

from random import choice, seed
from unittest import mock
from unittest.mock import Mock, patch

from pytest import raises
from pytest_randomly import default_seed

from src.name_builder.name_builder import NameBuilder, ParamType


@patch.object(NameBuilder, "get_forms")
@patch.object(NameBuilder, "get_list")
def test_generate_name(
    mock_get_list: Mock,
    mock_get_forms: Mock,
    parameters: ParamType,
) -> None:
    """A name_builder test."""
    print(f"setting the seed {default_seed}")
    seed(default_seed)

    forms: list[list[str]] = [
        ["parameter:name", "literal:eats", "adjective:flavor", "noun:fruit"],
    ]
    mock_get_forms.return_value = forms
    choice(forms)  # need to burn the seed

    items: list[list[str]] = [
        ["bitter", ""],
        ["salty", ""],
        ["sour", ""],
    ]
    expected_flavor: str = choice(items)[0]
    expected_fruit: str = choice(items)[0]
    mock_get_list.return_value = items
    expected_color: str = f"brian-eats-{expected_flavor}-{expected_fruit}"
    assert NameBuilder.generate_name(parameters, default_seed) == expected_color


@patch.object(NameBuilder, "get_forms")
def test_generate_name_form_dne(
    mock_get_forms: Mock,
    parameters: ParamType,
) -> None:
    """A name_builder test."""
    print(f"setting the seed {default_seed}")

    forms: list[list[str]] = [
        ["parameter:dne", "literal:eats", "adjective:flavor", "noun:fruit"],
    ]
    mock_get_forms.return_value = forms

    with raises(Exception):
        NameBuilder.generate_name(parameters, default_seed)


def test_get_forms() -> None:
    mock_open = mock.mock_open(read_data="red\nblue\nchartreuse")
    with patch("builtins.open", mock_open):
        assert [
            "chartreuse",
        ] in NameBuilder.get_forms()


def test_get_list() -> None:
    # data = "adjective, physics, color, colors.csv\nadjective, eaten, flavor, flavors.csv"
    data = "noun,food,fruit,fruits.csv\nnoun,food,hops,hops.csv"

    mock_open = mock.mock_open(read_data=data)
    expected_value = ["noun", "food", "fruit", "fruits.csv"]
    with patch("builtins.open", mock_open):
        assert expected_value in NameBuilder.get_list("noun", "fruit")
