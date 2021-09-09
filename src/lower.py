from .camel import camel_to_lower_case, is_camel_case
from .definitions import LOWER
from .exceptions import MixedCaseError
from .kebab import is_kebab_case, kebab_to_lower_case
from .pascal import is_pascal_case, pascal_to_lower_case
from .sentence import is_sentence_case, sentence_to_lower_case
from .snake import is_snake_case, snake_to_lower_case
from .title import is_title_case, title_to_lower_case
from .upper import is_upper_case, upper_to_lower_case


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
