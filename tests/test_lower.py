import pytest
from assertpy import assert_that
from src import is_lower_case, lower_case

from tests.loader import load_test_cases, select_case_match_tests, select_parser_tests

cases = load_test_cases()


@pytest.mark.parametrize("string,expected", select_parser_tests(cases, "lower"))
def test_lower_case(string: str, expected: str) -> None:
    assert_that(lower_case(string)).is_equal_to(expected)


@pytest.mark.parametrize("string,expected", select_case_match_tests(cases, "lower"))
def test_is_lower_case(string: str, expected: bool) -> None:
    assert_that(is_lower_case(string)).is_equal_to(expected)
