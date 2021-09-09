from functools import reduce

from .definitions import CAMEL


def is_camel_case(string: str) -> bool:
    return CAMEL.match(string) is not None


def lower_to_camel_case(lower: str) -> str:
    return "".join(
        [x if i == 0 else x.capitalize() for i, x in enumerate(lower.split(" "))]
    )


def camel_to_lower_case(camel: str) -> str:
    return reduce(
        lambda acc, x: acc + (" " + x.lower() if x.isupper() else x),
        camel,
        "",
    )
