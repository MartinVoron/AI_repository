"""Small demo app used to validate repository setup."""


def build_status_message() -> str:
    """Return the demo status message."""
    return "AI dev agent repository is initialized."


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def divide(a: float, b: float) -> float:
    """Return the division of two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def main() -> None:
    """Run the demo app."""
    print(build_status_message())


if __name__ == "__main__":
    main()
