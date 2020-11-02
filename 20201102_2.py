import typing


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
def ywords4(in_path: str):
    with open(in_path, "r") as fd:
        return set(word for line in fd for word in line.split())


for counter, value in enumerate(ywords4("data.txt")):
    print(f"{counter:d}: {value:s}")


