import pytest
from .loader import (load_test_cases, select_case_match_tests,
                     select_parser_tests)
from assertpy import assert_that
from src.convert import title_case
from src.title import is_title_case

cases = load_test_cases()


@pytest.mark.parametrize("string,expected", select_parser_tests(cases, "title"))
def test_title_case(string: str, expected: str) -> None:
    assert_that(title_case(string)).is_equal_to(expected)


@pytest.mark.parametrize("string,expected", select_case_match_tests(cases, "title"))
def test_is_title_case(string: str, expected: bool) -> None:
    assert_that(is_title_case(string)).is_equal_to(expected)
