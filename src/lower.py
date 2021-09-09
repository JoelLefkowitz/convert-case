from src.camel import camel_to_lower_case, is_camel_case
from src.definitions import LOWER
from src.exceptions import MixedCaseError
from src.kebab import is_kebab_case, kebab_to_lower_case
from src.pascal import is_pascal_case, pascal_to_lower_case
from src.sentence import is_sentence_case, sentence_to_lower_case
from src.snake import is_snake_case, snake_to_lower_case
from src.title import is_title_case, title_to_lower_case
from src.upper import is_upper_case, upper_to_lower_case


def lower_case(string: str) -> str:
    if is_lower_case(string):
        return string

    for (condition, parser) in [
        (is_upper_case, upper_to_lower_case),
        (is_sentence_case, sentence_to_lower_case),
        (is_title_case, title_to_lower_case),
        (is_camel_case, camel_to_lower_case),
        (is_snake_case, snake_to_lower_case),
        (is_kebab_case, kebab_to_lower_case),
        (is_pascal_case, pascal_to_lower_case),
    ]:
        if condition(string):
            return parser(string)

    raise MixedCaseError(string)


def is_lower_case(string: str) -> bool:
    return LOWER.match(string) is not None
