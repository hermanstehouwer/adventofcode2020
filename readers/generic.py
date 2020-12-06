def read_and_rstrip(file):
    with open(file) as f:
        for line in f:
            yield line.rstrip()


def yield_rstripped_and_joined_blocks(file):
    to_y = ""
    for line in read_and_rstrip(file):
        if line == "":
            yield to_y
            to_y = ""
        else:
            to_y = to_y+line
    yield to_y


def yield_blocks(file):
    with open(file) as f:
        data = f.read().split("\n\n")
        for d in data:
            yield d
