class MixedCaseError(Exception):
    def __init__(self, string: str) -> None:
        super().__init__(f"Could not parse the mixed case string: {string}")
