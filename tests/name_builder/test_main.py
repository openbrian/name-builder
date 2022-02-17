"""Test the main module in name_builder."""

from pytest import raises
from pytest_mock import MockerFixture

from src.name_builder import __main__
from src.name_builder.__main__ import NameBuilder, init, main


def test_main_should_call_name_builder(mocker: MockerFixture) -> None:
    mocked_do_something = mocker.patch.object(NameBuilder, "do_something")
    main()
    mocked_do_something.assert_called_once_with()


def test_init_should_call_main(mocker: MockerFixture) -> None:
    mocked_main = mocker.patch.object(__main__, "main")
    mocker.patch.object(__main__, "__name__", "__main__")
    with raises(SystemExit) as pytest_wrapped_e:
        init()
    assert pytest_wrapped_e.type == SystemExit
    mocked_main.assert_called_once_with()
