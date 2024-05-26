import pytest
from .loader import (load_test_cases, select_case_match_tests,
                     select_parser_tests)
from assertpy import assert_that
from src.convert import sentence_case
from src.sentence import is_sentence_case

cases = load_test_cases()


@pytest.mark.parametrize("string,expected", select_parser_tests(cases, "sentence"))
def test_sentence_case(string: str, expected: str) -> None:
    assert_that(sentence_case(string)).is_equal_to(expected)


@pytest.mark.parametrize("string,expected", select_case_match_tests(cases, "sentence"))
def test_is_sentence_case(string: str, expected: bool) -> None:
    assert_that(is_sentence_case(string)).is_equal_to(expected)
