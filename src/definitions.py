import re

LOWER = re.compile(r"^[a-z\s]*$")
UPPER = re.compile(r"^[A-Z\s]*$")

TITLE = re.compile(r"^(([A-Z][a-z]*)(\s[A-Z][a-z]*)*)?$")
SENTENCE = re.compile(r"^(([A-Z][a-z]*)(\s[a-z]*)*)?$")

CAMEL = re.compile(r"^([a-z][a-zA-Z]*)?$")
PASCAL = re.compile(r"^([A-Z]|([A-Z][a-z]+)*)?$")

SNAKE = re.compile(r"^([a-z]+(_[a-z]+)*)?$")
KEBAB = re.compile(r"^([a-z]+(-[a-z]+)*)?$")
