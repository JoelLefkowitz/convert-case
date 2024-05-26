import pytest
from .loader import (load_test_cases, select_case_match_tests,
                     select_parser_tests)
from assertpy import assert_that
from src.convert import upper_case
from src.upper import is_upper_case

cases = load_test_cases()


@pytest.mark.parametrize("string,expected", select_parser_tests(cases, "upper"))
def test_upper_case(string: str, expected: str) -> None:
    assert_that(upper_case(string)).is_equal_to(expected)


@pytest.mark.parametrize("string,expected", select_case_match_tests(cases, "upper"))
def test_is_upper_case(string: str, expected: bool) -> None:
    assert_that(is_upper_case(string)).is_equal_to(expected)
