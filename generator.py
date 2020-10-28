import typing
import sys


def fgen(f: typing.Callable[[int], int], x: int) -> typing.Generator[int, None, None]:
    first: bool = True
    last_value: int = x
    while True:
        if first:
            first = False
            yield last_value
        else:
            last_value = f(last_value)
            yield last_value


# Expected: 3, 2*3, 2*2*3, 2*2*2*3

v: int
for v in fgen(lambda x: 2*x, 3):
    print(f"{v:d}")
    sys.stdout.flush()
