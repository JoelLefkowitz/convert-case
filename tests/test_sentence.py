import pytest
from assertpy import assert_that

from src import is_sentence_case, sentence_case
from tests.loader import (load_test_cases, select_case_match_tests,
                          select_parser_tests)

cases = load_test_cases()


@pytest.mark.parametrize("string,expected", select_parser_tests(cases, "sentence"))
def test_sentence_case(string: str, expected: str) -> None:
    assert_that(sentence_case(string)).is_equal_to(expected)


@pytest.mark.parametrize("string,expected", select_case_match_tests(cases, "sentence"))
def test_is_sentence_case(string: str, expected: bool) -> None:
    assert_that(is_sentence_case(string)).is_equal_to(expected)
