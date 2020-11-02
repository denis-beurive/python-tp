import typing
import sys


# x, f(x), f(f(x)), f(f(f(x)))...

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


# x, f(x), f(f(x)), f(f(f(x)))...
def fgen2(f: typing.Callable[[int], int], x: int) -> typing.Generator[int, None, None]:
    def sub(f: typing.Callable[[int], int], x: int, count: int):
        if 0 == count:
            return x
        else:
            return f(x)

    c: int = 0
    while True:
        v: int = sub(f, x, c)
        yield v
        c += 1
        x = v


def fgen3(f: typing.Callable[[typing.Any], typing.Any], x: typing.Any) -> typing.Generator[typing.Any, None, None]:
    yield x
    while True:
        v: typing.Any = f(x)
        yield v
        x = v

# Expected: 3, 2*3, 2*2*3, 2*2*2*3

v: int
for v in fgen3(lambda x: 2*x, 3):
    print(f"{v:d}")
    sys.stdout.flush()
