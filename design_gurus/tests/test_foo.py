from typing import Callable


def check_result(foo: Callable, data: list[list | tuple]) -> None:
    for value, expected in data:
        result = foo(value)
        assert (
            result == expected
        ), f"{value} - got {result}, expected {expected}"
    print("ok!")
