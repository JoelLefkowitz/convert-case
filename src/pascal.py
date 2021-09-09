from functools import reduce

from .definitions import PASCAL


def is_pascal_case(string: str) -> bool:
    return PASCAL.match(string) is not None


def lower_to_pascal_case(lower: str) -> str:
    return "".join([i.capitalize() for i in lower.split(" ")])


def pascal_to_lower_case(pascal: str) -> str:
    return reduce(
        lambda acc, x: acc + (" " + x.lower() if x.isupper() else x),
        pascal,
        "",
    ).lstrip()
