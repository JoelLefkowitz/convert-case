import os
from .exceptions import MissingTestCases
from functools import reduce
from typing import Dict, List, Tuple


def load_test_cases() -> Dict[str, List[str]]:
    cases = {}

    with open(
        os.path.normpath(os.path.join(__file__, "..", "tests.md")), "r", encoding="utf8"
    ) as stream:
        table = stream.readlines()[2:]
        pipes = [i for i, x in enumerate(table[0]) if x == "|"]
        divisions = [(pipes[i] + 2, pipes[i + 1] - 1) for i in range(len(pipes) - 1)]

        for (i, j) in divisions:
            col = table[0][i:j].rstrip()
            cells = [row[i:j].rstrip() for row in table[2:]]
            cases[col] = cells

    return cases


def select_parser_tests(
    cases: Dict[str, List[str]], name: str
) -> List[Tuple[str, str]]:
    if not name in cases:
        raise MissingTestCases(name)

    return list(zip(cases["test"], cases[name]))


def select_case_match_tests(
    cases: Dict[str, List[str]], name: str
) -> List[Tuple[str, bool]]:
    return list(
        reduce(
            lambda acc, x: acc | {(x[0], True) if x[0] == x[1] else (x[0], False)},  # type: ignore
            select_parser_tests(cases, name),
            {("", True)},
        )
    )
