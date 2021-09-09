from .definitions import TITLE


def is_title_case(string: str) -> bool:
    return TITLE.match(string) is not None


def lower_to_title_case(lower: str) -> str:
    return " ".join([i.capitalize() for i in lower.split(" ")])


def title_to_lower_case(title: str) -> str:
    return title.lower()
