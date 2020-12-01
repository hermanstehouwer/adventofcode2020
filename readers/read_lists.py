from contextlib import contextmanager


@contextmanager
def read_list_ints(filename:str):
    with open(filename) as f:
        data = f.readlines()
    data = [int(x) for x in data]
    yield data
