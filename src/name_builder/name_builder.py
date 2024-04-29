"""The Foo module provides things and functions."""

from csv import reader
from random import choice, seed
from typing import Optional

ParamType = dict[str, str]


# pylint: disable=too-few-public-methods
class NameBuilder:
    """The Foo class provides sample methods."""

    @staticmethod
    def generate_name(
        parameters: ParamType,
        the_seed: Optional[int] = None,
        form_: Optional[list[str]] = None,
    ) -> str:
        if seed is not None:
            seed(the_seed)
        form: list[str] = (
            form_ if form_ is not None else list(choice(NameBuilder.get_forms()))
        )
        print(form)
        result = []
        for term in form:
            operator, value = term.split(":")
            if operator == "literal":
                result.append(value)
            elif operator == "parameter":
                param_val: Optional[str] = parameters.get(value)
                if param_val is None:
                    raise KeyError(f"Could not find parameter {value}.")
                result.append(param_val)
            elif operator in ("adjective", "noun"):
                lst = NameBuilder.get_list(operator, value)
                result.append(choice(lst)[0])
        return "-".join(result).lower()

    @staticmethod
    def get_forms() -> list[list[str]]:
        with open("src/name_builder/forms.csv", encoding="utf-8") as file:
            return list(reader(file))

    @staticmethod
    def get_list(operator_: str, name: str) -> list[list[str]]:
        # print(f"get_list({operator_}, {name})")
        with open("src/name_builder/lists.csv", encoding="utf-8") as lists_file:
            lists = list(reader(lists_file))
        # print(lists)
        filename: Optional[str] = None
        # Currently ignoring the second item.
        for operator, _, list_name, listfile in lists:
            if operator == operator_ and name == list_name:
                filename = listfile
                break
        filename = f"src/name_builder/data/{filename}"
        with open(filename, encoding="utf-8") as file:
            return list(reader(file))
