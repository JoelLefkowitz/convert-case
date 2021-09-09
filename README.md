# Convert Case

Convert between string cases with built-in case inference.

## Status

| Source     | Shields                                                                                                                                       |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Project    | ![release][release_shield] ![license][license_shield] ![lines][lines_shield] ![languages][languages_shield]                                   |
| Health     | ![readthedocs][readthedocs_shield] ![github_review][github_review_shield] ![codacy][codacy_shield] ![codacy_coverage][codacy_coverage_shield] |
| Publishers | ![pypi][pypi_shield] ![pypi_downloads][pypi_downloads_shield]                                                                                 |
| Repository | ![issues][issues_shield] ![issues_closed][issues_closed_shield] ![pulls][pulls_shield] ![pulls_closed][pulls_closed_shield]                   |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield]                            |

## Installing

```bash
pip install convert_case
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
LOWER = re.compile(r"^[a-z\s]*$")
UPPER = re.compile(r"^[A-Z\s]*$")

TITLE = re.compile(r"^(([A-Z][a-z]*)(\s[A-Z][a-z]*)*)?$")
SENTENCE = re.compile(r"^(([A-Z][a-z]*)(\s[a-z]*)*)?$")

CAMEL = re.compile(r"^([a-z][a-zA-Z]*)?$")
PASCAL = re.compile(r"^([A-Z]|([A-Z][a-z]+)*)?$")

SNAKE = re.compile(r"^([a-z]+(_[a-z]+)*)?$")
KEBAB = re.compile(r"^([a-z]+(-[a-z]+)*)?$")
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

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [contributing](CONTRIBUTING.md) for details on the process for submitting pull requests. Moreover, our [code of conduct](CODE_OF_CONDUCT.md) declares our collaboration standards.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][author]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Public links -->

[semver]: http://semver.org/
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[readthedocs]: https://convert_case.readthedocs.io/en/latest/

<!-- Acknowledgments -->

[author]: https://github.com/joellefkowitz

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

[pypi_shield]: https://img.shields.io/pypi/v/convert_case
[pypi_downloads_shield]: https://img.shields.io/pypi/dm/convert_case

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/convert-case
[issues_closed_shield]: https://img.shields.io/github/issues-closed/joellefkowitz/convert-case
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/convert-case
[pulls_closed_shield]: https://img.shields.io/github/issues-pr-closed/joellefkowitz/convert-case

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/convert-case
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/convert-case
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/convert-case
