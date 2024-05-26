class MissingTestCases(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Could not find test cases with name: {name}")
