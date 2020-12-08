import copy
from abc import abstractmethod, ABC
from enum import Enum
from typing import NamedTuple, List, Iterable, Dict


class ConsoleMemory:
    accumulator: int
    instruction_ptr: int

    def __init__(self, acc: int, ptr: int):
        self.accumulator = acc
        self.instruction_ptr = ptr


class Opcode(Enum):
    NOP = 0
    ACC = 1
    JMP = 2


class Instruction():
    operation: Opcode
    argument: int

    def __init__(self, op: Opcode, arg: int):
        self.operation = op
        self.argument = arg

    def __str__(self):
        return f"{self.operation}: {self.argument}"


class Operation(ABC):
    @abstractmethod
    def apply_operation(self, core: ConsoleMemory, instruction: Instruction):
        pass


class NOPOperation(Operation):
    def apply_operation(self, core: ConsoleMemory, instruction: Instruction):
        core.instruction_ptr += 1


class ACCOperation(Operation):
    def apply_operation(self, core: ConsoleMemory, instruction: Instruction):
        core.instruction_ptr += 1
        core.accumulator += instruction.argument


class JMPOperation(Operation):
    def apply_operation(self, core: ConsoleMemory, instruction: Instruction):
        core.instruction_ptr += instruction.argument


class Console:
    core: ConsoleMemory
    instructions: List[Instruction]
    visited: List[int]
    operations: Dict[Opcode, Operation]

    @staticmethod
    def _parse_instruction(instruction: str) -> Instruction:
        op, val = instruction.split(" ")
        opcode = Opcode.NOP
        if op == "acc":
            opcode = Opcode.ACC
        if op == "jmp":
            opcode = Opcode.JMP
        return Instruction(opcode, int(val))

    def __init__(self, instructions: Iterable[str]):
        self.core = ConsoleMemory(0, 0)
        self.instructions = []
        self.visited = []
        for instruction in instructions:
            self.instructions.append(self._parse_instruction(instruction))
        self.operations = {
            Opcode.NOP: NOPOperation(),
            Opcode.ACC: ACCOperation(),
            Opcode.JMP: JMPOperation()
        }

    def will_repeat(self):
        return self.core.instruction_ptr in self.visited

    def step(self):
        self.visited.append(self.core.instruction_ptr)
        instruction = self.instructions[self.core.instruction_ptr]
        self.operations[instruction.operation].apply_operation(self.core, instruction)

    def reset(self):
        self.core = ConsoleMemory(0, 0)
        self.visited = []

    def current_value(self) -> int:
        return self.core.accumulator

    # Day8 Part 1 method
    def run_until_repeat_instruction(self):
        while not self.will_repeat():
            self.step()

    # Day8 Part 2 methods
    def patch(self, index: int) -> bool:
        to_patch = self.instructions[index]
        if to_patch.operation == Opcode.NOP:
            to_patch.operation = Opcode.JMP
            return True
        if to_patch.operation == Opcode.JMP:
            to_patch.operation = Opcode.NOP
            return True
        return False

    def patch_and_check(self, index: int) -> bool:
        if not self.patch(index):
            return False
        while not self.will_repeat():
            if self.core.instruction_ptr >= len(self.instructions):
                return True
            self.step()
        return False

    def try_jmpnoppatching_until_terminates_normally(self):
        instructions = self.instructions
        for index in range(len(instructions)):
            self.reset()
            self.instructions = copy.deepcopy(instructions)
            if self.patch_and_check(index):
                return


