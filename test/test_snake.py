import pytest
from .loader import (load_test_cases, select_case_match_tests,
                     select_parser_tests)
from assertpy import assert_that
from src.convert import snake_case
from src.snake import is_snake_case

cases = load_test_cases()


@pytest.mark.parametrize("string,expected", select_parser_tests(cases, "snake"))
def test_snake_case(string: str, expected: str) -> None:
    assert_that(snake_case(string)).is_equal_to(expected)


@pytest.mark.parametrize("string,expected", select_case_match_tests(cases, "snake"))
def test_is_snake_case(string: str, expected: bool) -> None:
    assert_that(is_snake_case(string)).is_equal_to(expected)
