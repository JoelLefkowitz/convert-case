import pytest
from src import lower_case
from src.exceptions import MixedCaseError


def test_mixed_case() -> None:
    with pytest.raises(MixedCaseError):
        lower_case("A-B_C")
