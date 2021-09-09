from .definitions import SENTENCE


def is_sentence_case(string: str) -> bool:
    return SENTENCE.match(string) is not None


def lower_to_sentence_case(lower: str) -> str:
    return lower.capitalize()


def sentence_to_lower_case(sentence: str) -> str:
    return sentence.lower()
