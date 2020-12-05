def read_and_rstrip(file):
    with open(file) as f:
        for line in f:
            yield line.rstrip()
