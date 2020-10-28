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
t = (10, 11, 13, 15)
print(npair(*t))

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


# --------------------------------------------------------------
# Conversions
# --------------------------------------------------------------

# Tuple => List
my_tuple = (10, 20, 30)
print("my_tuple is a tuple? {:s}".format("yes" if isinstance(my_tuple, typing.Tuple) else "no"))
my_list = [v for v in my_tuple]
print("my_list is a list? {:s}".format("yes" if isinstance(my_list, typing.List) else "no"))
print(repr(my_list))

# List = Tuple
my_tuple = tuple([1, 3, 10])
print("my_tuple is a Tuple? {:s}".format("yes" if isinstance(my_tuple, typing.Tuple) else "no"))
my_tuple = (list,)
print("my_tuple is a Tuple? {:s}".format("yes" if isinstance(my_tuple, typing.Tuple) else "no"))
my_tuple = tuple(v for v in [1, 3, 10])
print("my_tuple is a Tuple? {:s}".format("yes" if isinstance(my_tuple, typing.Tuple) else "no"))

# List => Generator
my_generator = (v for v in my_list)
print("my_generator is a generator? {:s}".format("yes" if isinstance(my_generator, typing.Generator) else "no"))
print("my_generator is a list? {:s}".format("yes" if isinstance(my_generator, typing.List) else "no"))


# --------------------------------------------------------------
# Rot 13
# --------------------------------------------------------------


def rot13(in_string: str):
    result_list: list = []
    for c in list(in_string):
        if 'A' <= c <= 'Z':
            result_list.append(chr((ord(c)-ord('A')-13) % 26 + ord('A')))
            continue
        if 'a' <= c <= 'z':
            result_list.append(chr((ord(c)-ord('a')-13) % 26 + ord('a')))
            continue
        result_list.append(c)
    return "".join(result_list)


print(rot13("NZ nz"))

# Generate a "table for the rotation"
table1 = [c for c in range(0, ord('A'))]
table2 = [chr((c-ord('A')-13) % 26 + ord('A')) for c in range(ord('A'), ord('Z')+1)]
table3 = [c for c in range(ord('Z')+1, ord('a'))]
table4 = [chr((c-ord('a')-13) % 26 + ord('a')) for c in range(ord('a'), ord('z')+1)]
table5 = [c for c in range(ord('z')+1, 256)]

table = [*table1, *table2, *table3, *table4, *table5]
print("count: {:d}".format(table1.__len__()))
print("count: {:d}".format(table2.__len__()))
print("count: {:d}".format(table3.__len__()))
print("count: {:d}".format(table4.__len__()))
print("count: {:d}".format(table5.__len__()))
print("count: {:d}".format(table.__len__()))
print(table)


def uwords(in_path: str) -> typing.List[str]:
    words: typing.Set[str] = set([])
    fd: typing.TextIO = open(in_path, "r")
    for line in fd:
        words.update(line.split())
    fd.close()
    return list(words)


print(uwords("data.txt"))



