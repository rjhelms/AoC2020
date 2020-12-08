from copy import deepcopy
from dataclasses import dataclass
from typing import List


@dataclass
class Instruction:
    operation: str
    value: int
    count: int = 0


class Computer:
    pointer: int
    accumulator: int
    program: List[Instruction]
    operations: dict

    def __init__(self, program: List[Instruction]):
        self.pointer = 0
        self.accumulator = 0
        self.program = program

        # is it possible to declare this statically?
        self.operations = {"nop": self.nop, "acc": self.acc, "jmp": self.jmp}

    def nop(self, value):
        self.pointer += 1

    def acc(self, value):
        self.accumulator += value
        self.pointer += 1

    def jmp(self, value):
        self.pointer += value

    def execute(self):
        # if count > 0 there's an infinite loop
        while self.program[self.pointer].count == 0:
            instruction = self.program[self.pointer]
            instruction.count += 1
            self.operations[instruction.operation](instruction.value)
            # return True if pointer is past end of program, ie program halts
            if self.pointer >= len(self.program):
                return True
        return False


if __name__ == "__main__":
    original_program = []
    with open("8a.txt", "r") as f:
        data = f.read().splitlines()
        for line in data:
            split = line.split(" ")
            operation = split[0]
            value = int(split[1])
            original_program.append(Instruction(operation, value))

    for i in range(len(original_program)):
        # deepcopy to make copies of Instructions as well as the list
        program = deepcopy(original_program)
        if original_program[i].operation == "nop":
            program[i].operation = "jmp"
        elif original_program[i].operation == "jmp":
            program[i].operation = "nop"
        else:
            continue

        computer = Computer(program)
        if computer.execute():
            print(computer.accumulator)
            break
