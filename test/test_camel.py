import pytest
from .loader import (load_test_cases, select_case_match_tests,
                     select_parser_tests)
from assertpy import assert_that
from src.camel import is_camel_case
from src.convert import camel_case

cases = load_test_cases()


@pytest.mark.parametrize("string,expected", select_parser_tests(cases, "camel"))
def test_camel_case(string: str, expected: str) -> None:
    assert_that(camel_case(string)).is_equal_to(expected)


@pytest.mark.parametrize("string,expected", select_case_match_tests(cases, "camel"))
def test_is_camel_case(string: str, expected: bool) -> None:
    assert_that(is_camel_case(string)).is_equal_to(expected)
