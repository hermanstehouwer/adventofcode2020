from typing import Iterable, Tuple


def get_new_direction(d: str, action: str)-> str:
    rotate = int(action[1:])
    directions = {"N":0, "S": 180, "E": 90, "W": 270}
    reverse_lookup = {0:"N", 180:"S", 90:"E", 270:"W"}
    if action[0] == "L":
        rotate = 360 - rotate
    direction = directions[d]
    direction = (direction + rotate) % 360
    return reverse_lookup[direction]


def action_to_direction(actions: Iterable[str]) -> Iterable[str]:
    d = "E"
    for action in actions:
        if action[0] in ["N", "S", "E", "W"]:
            yield action
        elif action[0] == "F":
            yield d + action[1:]
        else:
            d = get_new_direction(d, action)


def get_coordinates(directions: Iterable[str]) -> Iterable[Tuple[int, int]]:
    x, y = 0, 0
    for d in directions:
        amount = int(d[1:])
        direction = d[0]
        if direction == "N":
            y += amount
        elif direction == "S":
            y -= amount
        elif direction == "E":
            x += amount
        elif direction == "W":
            x -= amount
        else:
            raise ValueError(d)
        yield x, y


def rotate_wp(WP: Tuple[int, int], amount: int) -> Tuple[int, int]:
    print(f"Rotating {WP} {amount}degrees right: ")
    if amount == 90:
        WP = WP[1], -WP[0]
    elif amount == 180:
        WP = -WP[0], -WP[1]
    elif amount == 270:
        WP = -WP[1], WP[0]
    else:
        raise ValueError(f"INVALID AMOUNT: {amount}")
    print(f"Result: {WP}")
    return WP


def get_coordinates2(directions: Iterable[str]) -> Iterable[Tuple[int, int]]:
    WP = (10, 1)
    C = (0, 0)
    for d in directions:
        amount = int(d[1:])
        direction = d[0]
        if direction == "N":
            WP = (WP[0], WP[1] + amount)
        elif direction == "S":
            WP = (WP[0], WP[1] - amount)
        elif direction == "E":
            WP = (WP[0] + amount, WP[1])
        elif direction == "W":
            WP = (WP[0] - amount, WP[1])
        elif direction == "F":
            C = (C[0] + WP[0]*amount, C[1] + WP[1]*amount)
            yield C
        elif direction == "R":
            print(f"{d}")
            WP = rotate_wp(WP, amount)
        elif direction == "L":
            print(f"{d}")
            WP = rotate_wp(WP, 360 - amount)
        else:
            raise ValueError(d)


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs (y1 - y2)