from .definitions import SNAKE


def is_snake_case(string: str) -> bool:
    return SNAKE.match(string) is not None


def lower_to_snake_case(lower: str) -> str:
    return "_".join(lower.split(" "))


def snake_to_lower_case(snake: str) -> str:
    return " ".join(snake.split("_"))
