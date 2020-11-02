import typing


def ywords1(in_path: str) -> typing.Set[str]:
    uniq_words: typing.Set[str] = set()
    with open(in_path, "r") as fd:
        line: str
        for line in fd:
            uniq_words.update(iter(line.split()))
    return uniq_words


def ywords2(in_path: str):
    with open(in_path, "r") as fd:
        line: str
        for line in fd:
            for w in line.split():
                yield w


# This is the good solution
def ywords3(in_path: str):
    result = set()
    with open(in_path, "r") as fd:
        result.update(set(word for line in fd for word in line.split()))
    return result


for counter, value in enumerate(ywords3("data.txt")):
    print(f"{counter:d}: {value:s}")


