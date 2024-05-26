import pytest
from .loader import (load_test_cases, select_case_match_tests,
                     select_parser_tests)
from assertpy import assert_that
from src.convert import kebab_case
from src.kebab import is_kebab_case

cases = load_test_cases()


@pytest.mark.parametrize("string,expected", select_parser_tests(cases, "kebab"))
def test_kebab_case(string: str, expected: str) -> None:
    assert_that(kebab_case(string)).is_equal_to(expected)


@pytest.mark.parametrize("string,expected", select_case_match_tests(cases, "kebab"))
def test_is_kebab_case(string: str, expected: bool) -> None:
    assert_that(is_kebab_case(string)).is_equal_to(expected)
