from src.camel import lower_to_camel_case
from src.kebab import lower_to_kebab_case
from src.lower import lower_case
from src.pascal import lower_to_pascal_case
from src.sentence import lower_to_sentence_case
from src.snake import lower_to_snake_case
from src.title import lower_to_title_case
from src.upper import lower_to_upper_case


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
