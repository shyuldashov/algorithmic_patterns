from typing import Any


def test_for_two_pointers(foo, data: list[tuple[Any, Any, Any]]) -> None:
    for values, target, expected in data:
        result = foo(values, target)

        assert (
            result == expected
        ), f"{values}, {target} - got {result}, expected {expected}"

    print("ok")
