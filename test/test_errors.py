import pytest
from src.exceptions import MixedCaseError
from src.lower import lower_case


def test_mixed_case() -> None:
    with pytest.raises(MixedCaseError):
        lower_case("A-B_C")
