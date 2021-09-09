from .definitions import UPPER


def is_upper_case(string: str) -> bool:
    return UPPER.match(string) is not None


def lower_to_upper_case(lower: str) -> str:
    return lower.upper()


def upper_to_lower_case(upper: str) -> str:
    return upper.lower()
