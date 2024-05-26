# Convert case

Convert between string cases with built-in case inference.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/convert-case/review.yml)
![Version](https://img.shields.io/pypi/v/convert-case)
![Downloads](https://img.shields.io/pypi/dw/convert-case)
![Quality](https://img.shields.io/codacy/grade/3b8afbb8327d424b9990741fd587d7c4)
![Coverage](https://img.shields.io/codacy/coverage/3b8afbb8327d424b9990741fd587d7c4)

## Installation

```bash
pip install convert-case
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/convert-case).

## Usage

```python
from convert_case import camel_case

camel_case('camel case') # Inferred: lower -> camel
'camelCase'

camel_case('Camel Case') # Inferred: title -> camel
'camelCase'

camel_case('CamelCase') # Inferred: pascal -> camel
'camelCase'
```

### Exports

```python
def pascal_case(string: str) -> str:
    ...
def is_pascal_case(string: str) -> bool:
    ...

def camel_case(string: str) -> str:
    ...
def is_camel_case(string: str) -> bool:
    ...

def kebab_case(string: str) -> str:
    ...
def is_kebab_case(string: str) -> bool:
    ...

def sentence_case(string: str) -> str:
    ...
def is_sentence_case(string: str) -> bool:
    ...

def snake_case(string: str) -> str:
    ...
def is_snake_case(string: str) -> bool:
    ...

def title_case(string: str) -> str:
    ...
def is_title_case(string: str) -> bool:
    ...

def upper_case(string: str) -> str:
    ...
def is_upper_case(string: str) -> bool:
    ...
```

### Definitions

```python
LOWER = re.compile(r"^[a-z0-9\s]*$")
UPPER = re.compile(r"^[A-Z0-9\s]*$")

TITLE = re.compile(r"^(([A-Z0-9][a-z0-9]*)(\s[A-Z0-9][a-z0-9]*)*)?$")
SENTENCE = re.compile(r"^(([A-Z0-9][a-z0-9]*)(\s[a-z0-9]*)*)?$")

CAMEL = re.compile(r"^([a-z0-9][a-zA-Z0-9]*)?$")
PASCAL = re.compile(r"^([A-Z0-9]|([A-Z0-9][a-z0-9]+)*)?$")

SNAKE = re.compile(r"^([a-z0-9]+(_[a-z0-9]+)*)?$")
KEBAB = re.compile(r"^([a-z0-9]+(-[a-z0-9]+)*)?$")
```

### Test cases

| test     | lower    | upper    | sentence | title    | camel  | snake    | kebab    | pascal |
| -------- | -------- | -------- | -------- | -------- | ------ | -------- | -------- | ------ |
| a        | a        | A        | A        | A        | a      | a        | a        | A      |
| A        | a        | A        | A        | A        | a      | a        | a        | A      |
| abc      | abc      | ABC      | Abc      | Abc      | abc    | abc      | abc      | Abc    |
| ab cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| Ab cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| Ab Cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| ab_cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| ab-cd    | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| abCd     | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| ABCD     | abcd     | ABCD     | Abcd     | Abcd     | abcd   | abcd     | abcd     | Abcd   |
| AbCd     | ab cd    | AB CD    | Ab cd    | Ab Cd    | abCd   | ab_cd    | ab-cd    | AbCd   |
| ab cd ef | ab cd ef | AB CD EF | Ab cd ef | Ab Cd Ef | abCdEf | ab_cd_ef | ab-cd-ef | AbCdEf |
| AbCdEf   | ab cd ef | AB CD EF | Ab cd ef | Ab Cd Ef | abCdEf | ab_cd_ef | ab-cd-ef | AbCdEf |
| ab-cd-ef | ab cd ef | AB CD EF | Ab cd ef | Ab Cd Ef | abCdEf | ab_cd_ef | ab-cd-ef | AbCdEf |
| Ab cd ef | ab cd ef | AB CD EF | Ab cd ef | Ab Cd Ef | abCdEf | ab_cd_ef | ab-cd-ef | AbCdEf |

#### Numbers

Numbers are treated as letters with no specific case.

| test | lower | upper | sentence | title | camel | snake | kebab | pascal |
| ---- | ----- | ----- | -------- | ----- | ----- | ----- | ----- | ------ |
| 1    | 1     | 1     | 1        | 1     | 1     | 1     | 1     | 1      |
| 1bc  | 1bc   | 1BC   | 1bc      | 1bc   | 1bc   | 1bc   | 1bc   | 1bc    |
| a1c  | a1c   | A1C   | A1c      | A1c   | a1c   | a1c   | a1c   | A1c    |
| ab1  | ab1   | AB1   | Ab1      | Ab1   | ab1   | ab1   | ab1   | Ab1    |
| a1 c | a1 c  | A1 C  | A1 c     | A1 C  | a1C   | a1_c  | a1-c  | A1C    |
| a1-c | a1 c  | A1 C  | A1 c     | A1 C  | a1C   | a1_c  | a1-c  | A1C    |

## Discussion

A goal of this converter is that it is deterministic. If we consider the following examples we can see that this is not simple to achieve. How should we interpret the string 'ABC', is it in upper case or pascal case?

| test  | upper | pascal |
| ----- | ----- | ------ |
| abc   | ABC   | Abc    |
| a b c | A B C | ABC    |

Our options are:

- To consider strings with consecutive capitals like 'ABC' not to be pascal case. If in this case 'a b c' is parsed to 'Abc' it would clash with parsing 'abc' into pascal case.

- To store some state that remembers the string's case before parsing. This would introduce too much complexity.

- To prioritize parsing the string as one case unless told otherwise. We choose to pick upper case as the inferred case. The caveat here is that we will no longer be performing 'round trip' conversion.

Round trip conversion:

```python
kebab_case('a b c')
'a-b-c'

lower_case('a-b-c')
'a b c'
```

Not round trip conversion:

```python
pascal_case('a b c')
'ABC'

lower_case('ABC')
'abc'
```

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
