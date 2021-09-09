from .definitions import KEBAB


def is_kebab_case(string: str) -> bool:
    return KEBAB.match(string) is not None


def lower_to_kebab_case(lower: str) -> str:
    return "-".join(lower.split(" "))


def kebab_to_lower_case(kebab: str) -> str:
    return " ".join(kebab.split("-"))
