import re
from typing import Dict, List


class BitMask:
    and_mask: int
    or_mask: int

    def __init__(self, bitmask_str: str):
        # X, 1, 0
        # 0 -> 0, X->1 in and_mask
        and_str = bitmask_str.replace("X", "1")
        self.and_mask = int(and_str, 2)
        # 0 -> 0, 1-> 1, X -> 0 in or_mask
        or_str = bitmask_str.replace("X", "0")
        self.or_mask = int(or_str, 2)

    def mask(self, to_mask: int) -> int:
        anded = to_mask & self.and_mask
        ored = anded | self.or_mask
        return ored


class BitMaskProcessor:
    memory: Dict[int, int]
    masks: List[BitMask]

    def __init__(self):
        self.memory = {}
        self.masks = []

    def sum_of_values(self):
        return sum(self.memory.values())

    def _make_masks(self, mask: str) -> None:
        todo = [mask.replace("0", "a").replace("1", "b")]
        self.masks = []
        while todo:
            curr = todo.pop()
            if "X" in curr:
                todo.append(curr.replace("X", "1", 1))
                todo.append(curr.replace("X", "0", 1))
            else:
                doit = curr.replace("a", "X").replace("b", "1")
                self.masks.append(BitMask(doit))

    def process_step(self, step: str, mode2=False):
        left, right = step.split(" = ")
        if left == "mask":
            if not mode2:
                self.masks = [BitMask(right)]
            else:
                self._make_masks(right)
        else:
            val = int(right)
            m = re.match(r'.*\[(.*)].*', left)
            tgt = int(m.group(1))
            if not mode2:
                self.memory[tgt] = self.masks[0].mask(val)
            else:
                for mask in self.masks:
                    ntgt = mask.mask(tgt)
                    self.memory[mask.mask(tgt)] = val
