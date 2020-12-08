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
        # if count > 1 there's an infinite loop
        while self.program[self.pointer].count == 0:
            instruction = self.program[self.pointer]
            instruction.count += 1
            print(self.pointer, instruction.operation, instruction.value)
            self.operations[instruction.operation](instruction.value)

        return self.accumulator


if __name__ == "__main__":
    program = []
    with open("8a.txt", "r") as f:
        data = f.read().splitlines()
        for line in data:
            split = line.split(" ")
            operation = split[0]
            value = int(split[1])
            program.append(Instruction(operation, value))

    computer = Computer(program)
    print(computer.execute())
