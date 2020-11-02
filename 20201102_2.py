import typing
import collections


# This solution does not use a comprehension
def ywords1(in_path: str) -> typing.Set[str]:
    uniq_words: typing.Set[str] = set()
    with open(in_path, "r") as fd:
        line: str
        for line in fd:
            uniq_words.update(iter(line.split()))
    return uniq_words


# This is just fot test.
def words_yield(in_path: str):
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

def ywords4(in_path: str):
    with open(in_path, "r") as fd:
        return set(word for line in fd for word in line.split())


for counter, value in enumerate(ywords4("data.txt")):
    print(f"{counter:d}: {value:s}")


def count_words1(in_path: str):
    result = collections.defaultdict(int)
    with open(in_path, "r") as fd:
        for line in fd:
            for word in line.split():
                result[word] += 1
    return result


for counter, value in enumerate(count_words1("data.txt")):
    print(f"{counter:d}: {value:s}")


# This solution uses a Counter object.
def count_words2(in_path: str):
    result = collections.Counter()
    with open(in_path, "r") as fd:
        for line in fd:
            result.update(line.split())
    return result


# This solution is the best one.
def count_words3(in_path: str):
    with open(in_path, "r") as fd:
        return collections.Counter(word for line in fd for word in line.split())


print(count_words3("data.txt"))





