import typing

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------


def factorial(n):
    if 0 == n:
        return 1
    return n * factorial(n-1)


n = 3
# Python 3
print('factorial({:d})={:d}'.format(n, factorial(n)))
# Python 3.6 and greater
print(f'factorial({n:d})={factorial(n):n}')


def p_factorial(n, p):  # Accumulator
    if 0 == n:
        return p
    return p_factorial(n-1, p*n)


def p2_factorial(n: int, p: int = 1) -> int:  # Accumulator
    if 0 == n:
        return p
    # Note: p=p*n (this is best if we decide to add a new
    # parameter in the function signature)
    return p_factorial(n-1, p=p*n)


print(p2_factorial(3))


# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------


def pair(iterable: typing.Iterable[int]) -> typing.List[int]:
    result: typing.List[int] = []
    v: int
    for v in iterable:
        if v % 2 == 0:
            result.append(v)
    return result


print(pair(range(0, 20)))


def npair(*in_args: int) -> typing.List[int]:
    result: typing.List[int] = []
    v: int
    for v in in_args:
        if v % 2 == 0:
            result.append(v)
    return result


print(npair(10, 20, 30, 40))

# --------------------------------------------------------------
# Create an iterable
# --------------------------------------------------------------


class MyIterable:
    min: int
    max: int

    def __init__(self, in_min: int, in_max: int):
        self.min = in_min
        self.max = in_max

    def __iter__(self) -> typing.Iterable[int]:
        return self

    def __next__(self) -> int:
        if self.min >= self.max:
            raise StopIteration
        else:
            v, self.min = self.min, self.min + 1
            return v


my_iterable: MyIterable = MyIterable(0, 10)
print("Is iterable ? {:s}".format("yes" if isinstance(my_iterable, typing.Iterable) else "no"))
print("Has __iter__() ? {:s}".format("yes" if hasattr(MyIterable, '__iter__') and callable(MyIterable.__iter__) else "no"))
print("Has __next__() ? {:s}".format("yes" if hasattr(MyIterable, '__next__') and callable(MyIterable.__iter__) else "no"))


for v in my_iterable:
    print(f"{v:d}")




