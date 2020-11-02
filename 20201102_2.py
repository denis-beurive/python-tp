import typing
import collections
import math


# This solution does not use a comprehension
def ywords1(in_path: str) -> typing.Set[str]:
    uniq_words: typing.Set[str] = set()
    fd: typing.TextIO
    with open(in_path, "r") as fd:
        line: str
        for line in fd:
            uniq_words.update(iter(line.split()))
    return uniq_words


# This is just fot test.
def words_yield(in_path: str) -> typing.Generator[str, None, None]:
    fd: typing.TextIO
    with open(in_path, "r") as fd:
        line: str
        for line in fd:
            for w in line.split():
                yield w


# This is the good solution
# Note:
#
#       for line in fd:
#           for word in line.split():
#               ...
#
# => set(word for line in fd for word in line.split())
#
# Generalisation:
#
#       for A in B:
#           for C in D:
#               ...
#
# => set(C for A in B for C in D)

def ywords4(in_path: str) -> typing.Set[str]:
    fd: typing.TextIO
    with open(in_path, "r") as fd:
        return set(word for line in fd for word in line.split())


for counter, value in enumerate(ywords4("data.txt")):
    print(f"{counter:d}: {value:s}")

# -----------------------------------------------
# Using defaultdict.
# -----------------------------------------------


def count_words1(in_path: str):
    result = collections.defaultdict(int)
    fd: typing.TextIO
    with open(in_path, "r") as fd:
        line: str
        for line in fd:
            for word in line.split():
                result[word] += 1
    return result


for counter, value in enumerate(count_words1("data.txt")):
    print(f"{counter:d}: {value:s}")


# -----------------------------------------------
# Using counters.
# -----------------------------------------------

# This solution uses a Counter object. But it could be better.
def count_words2(in_path: str) -> typing.Counter[str]:
    result = collections.Counter()
    fd: typing.TextIO
    with open(in_path, "r") as fd:
        line: str
        for line in fd:
            result.update(line.split())
    return result


# This solution is the best one.
def count_words3(in_path: str) -> typing.Counter[str]:
    fd: typing.TextIO
    with open(in_path, "r") as fd:
        word: str
        line: str
        return collections.Counter(word for line in fd for word in line.split())


print(count_words3("data.txt"))


# -----------------------------------------------
# ZIP ans dictionary.
# -----------------------------------------------

# Create a dict for 2 lists. A list of keys and a list of values.
def create_dict(keys: list, values: list) -> dict:
    return dict(zip(keys, values))


print(create_dict(["a", "b"], [10, 20]))


# -----------------------------------------------
# Class.
# -----------------------------------------------


class V:

    def __init__(self, *args: int):
        self.vector = list(args)

    def __repr__(self) -> str:
        return f'V({", ".join([f"{x:d}" for x in self.vector]):s})'

    def __abs__(self) -> float:
        return math.sqrt(sum([x ** 2 for x in self.vector]))

    def __len__(self) -> int:
        return len(self.vector)


v = V(10, 20, 30)
print(len(v))
print(v)
print(abs(v))




