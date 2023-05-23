import re

LOWER = re.compile(r"^[a-z0-9\s]*$")
UPPER = re.compile(r"^[A-Z0-9\s]*$")

TITLE = re.compile(r"^(([A-Z0-9][a-z0-9]*)(\s[A-Z0-9][a-z0-9]*)*)?$")
SENTENCE = re.compile(r"^(([A-Z0-9][a-z0-9]*)(\s[a-z0-9]*)*)?$")

CAMEL = re.compile(r"^([a-z0-9][a-zA-Z0-9]*)?$")
PASCAL = re.compile(r"^([A-Z0-9]|([A-Z0-9][a-z0-9]+)*)?$")

SNAKE = re.compile(r"^([a-z0-9]+(_[a-z0-9]+)*)?$")
KEBAB = re.compile(r"^([a-z0-9]+(-[a-z0-9]+)*)?$")
