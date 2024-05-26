import pytest
from .loader import (load_test_cases, select_case_match_tests,
                     select_parser_tests)
from assertpy import assert_that
from src.convert import pascal_case
from src.pascal import is_pascal_case

cases = load_test_cases()


@pytest.mark.parametrize("string,expected", select_parser_tests(cases, "pascal"))
def test_pascal_case(string: str, expected: str) -> None:
    assert_that(pascal_case(string)).is_equal_to(expected)


@pytest.mark.parametrize("string,expected", select_case_match_tests(cases, "pascal"))
def test_is_pascal_case(string: str, expected: bool) -> None:
    assert_that(is_pascal_case(string)).is_equal_to(expected)
