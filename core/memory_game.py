from typing import List, Generator


def take_turns(numbers: List[int]) -> Generator[int, None, None]:
    lasttime: dict[int, int] = {}
    index = 0
    prev = 0
    for n in numbers:
        index += 1
        lasttime[n] = index
        prev = n
        yield n
    while True:
        new = lasttime.get(prev, 0)
        lasttime[prev] = index
        if new != 0:
            new = index - new
        prev = new
        index += 1
        yield new
