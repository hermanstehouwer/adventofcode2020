from contextlib import contextmanager


@contextmanager
def read_list_ints_sorted(filename:str):
    with open(filename) as f:
        data = f.readlines()
    data = [int(x) for x in data]
    data.sort()
    yield data
