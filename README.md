# Convert Case

Convert between string cases with built-in case inference.

## Status

| Source     | Shields                                                                                                                                      |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Project    | ![release][release_shield] ![license][license_shield] ![lines][lines_shield] ![languages][languages_shield]                                  |
| Health     | ![readthedocs][readthedocs_shield] ![github_review][github_review_shield]![codacy][codacy_shield] ![codacy_coverage][codacy_coverage_shield] |
| Publishers | ![pypi][pypi_shield] ![pypi_downloads][pypi_downloads_shield]                                                                                |
| Repository | ![issues][issues_shield] ![issues_closed][issues_closed_shield] ![pulls][pulls_shield] ![pulls_closed][pulls_closed_shield]                  |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield]                           |

## Installing

Install the package from pypi:

```bash
pip install convert-case
```

To experiment with the source code locally, clone the repository:

```bash
git clone https://github.com/joellefkowitz/convert-case
```

To install linters, formatters and test runners:

```bash
pip install .[all]
npm install
```

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

## Tests

To run unit tests:

```bash
grunt test
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

| test     | lower    | upper    | sentence | title    | camel  | snake    | kebab    | pascal |
| -------- | -------- | -------- | -------- | -------- | ------ | -------- | -------- | ------ |
| 1        | 1        | 1        | 1        | 1        | 1      | 1        | 1        | 1      |
| 1bc      | 1bc      | 1BC      | 1bc      | 1bc      | 1bc    | 1bc      | 1bc      | 1bc    |
| a1c      | a1c      | A1C      | A1c      | A1c      | a1c    | a1c      | a1c      | A1c    |
| ab1      | ab1      | AB1      | Ab1      | Ab1      | ab1    | ab1      | ab1      | Ab1    |
| a1 c     | a1 c     | A1 C     | A1 c     | A1 C     | a1C    | a1_c     | a1-c     | A1C    |
| a1-c     | a1 c     | A1 C     | A1 c     | A1 C     | a1C    | a1_c     | a1-c     | A1C    |

## Advanced

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

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

## Continuous integration

This repository uses github actions to lint and test each commit. Formatting tasks and writing/generating documentation must be done before committing new code.

## Versioning

This repository adheres to semantic versioning standards.
For more information on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [changelog](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [contributing](CONTRIBUTING.md) for details on the process for submitting pull requests. Moreover, our [code of conduct](CODE_OF_CONDUCT.md) declares our collaboration standards.

## Contributors

- **joellefkowitz** - _Initial work_ - [joellefkowitz][author]

[![Buy Me A Coffee][coffee_button]][author_coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Project links -->

[readthedocs]: https://convert-case.readthedocs.io/en/latest/

<!-- External links -->

[semver]: http://semver.org/
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Contributor links -->

[author]: https://github.com/joellefkowitz
[author_coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/convert-case
[license_shield]: https://img.shields.io/github/license/joellefkowitz/convert-case
[lines_shield]: https://img.shields.io/tokei/lines/github/joellefkowitz/convert-case
[languages_shield]: https://img.shields.io/github/languages/count/joellefkowitz/convert-case

<!-- Health shields -->

[readthedocs_shield]: https://img.shields.io/readthedocs/convert-case
[github_review_shield]: https://img.shields.io/github/workflow/status/JoelLefkowitz/convert-case/Review
[codacy_shield]: https://img.shields.io/codacy/grade/3b8afbb8327d424b9990741fd587d7c4
[codacy_coverage_shield]: https://img.shields.io/codacy/coverage/3b8afbb8327d424b9990741fd587d7c4

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/convert-case
[pypi_downloads_shield]: https://img.shields.io/pypi/dm/convert-case

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/convert-case
[issues_closed_shield]: https://img.shields.io/github/issues-closed/joellefkowitz/convert-case
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/convert-case
[pulls_closed_shield]: https://img.shields.io/github/issues-pr-closed/joellefkowitz/convert-case

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/convert-case
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/convert-case
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/convert-case
