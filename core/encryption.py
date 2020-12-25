from sympy.ntheory import discrete_log
SUBJECT_NUMBER = 7
MODULO = 20201227


def get_loop_size(public_key: int) -> int:
    return discrete_log(MODULO, public_key, SUBJECT_NUMBER)


def get_encryption_key(subject_number:int, loop_size: int) -> int:
    out = 1
    for _ in range(loop_size):
        out = (out*subject_number) % MODULO
    return out
