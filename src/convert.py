from .camel import lower_to_camel_case
from .kebab import lower_to_kebab_case
from .lower import lower_case
from .pascal import lower_to_pascal_case
from .sentence import lower_to_sentence_case
from .snake import lower_to_snake_case
from .title import lower_to_title_case
from .upper import lower_to_upper_case


def pascal_case(string: str) -> str:
    return lower_to_pascal_case(lower_case(string))


def camel_case(string: str) -> str:
    return lower_to_camel_case(lower_case(string))


def kebab_case(string: str) -> str:
    return lower_to_kebab_case(lower_case(string))


def sentence_case(string: str) -> str:
    return lower_to_sentence_case(lower_case(string))


def snake_case(string: str) -> str:
    return lower_to_snake_case(lower_case(string))


def title_case(string: str) -> str:
    return lower_to_title_case(lower_case(string))


def upper_case(string: str) -> str:
    return lower_to_upper_case(lower_case(string))
