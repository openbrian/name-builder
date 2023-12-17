"""Common fixtures for all tests."""
from pytest import fixture

from src.name_builder.name_builder import ParamType


@fixture(scope="module")
def parameters() -> ParamType:
    return {"name": "brian"}
