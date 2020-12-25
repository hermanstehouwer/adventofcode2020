from core.encryption import get_loop_size, get_encryption_key


def test_part1():
    public_key = 5764801
    assert get_loop_size(public_key) == 8
    door_key = 17807724
    assert get_loop_size(door_key) == 11
    assert get_encryption_key(17807724, 8) == 14897079
    assert get_encryption_key(5764801, 11) == 14897079
