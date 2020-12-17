from enum import Enum


class Field:
    def __init__(self, name, ranges):
        self.name = name
        self.ranges = []
        for range in ranges:
            self.ranges.append([int(value) for value in range.split("-")])

    def validate_number(self, number):
        for range in self.ranges:
            if number >= range[0] and number <= range[1]:
                return True
        return False


class ReadState(Enum):
    RULES = 1
    YOUR_TICKET = 2
    OTHER_TICKET = 3


if __name__ == "__main__":
    fields = []
    your_ticket = []
    other_tickets = []
    read_state = ReadState.RULES
    with open("16a.txt", "r") as f:
        data = f.read().splitlines()
        for line in data:
            if read_state == ReadState.RULES:
                if len(line) == 0:
                    read_state = ReadState.YOUR_TICKET
                    continue
                line = line.split(": ")
                rule_name = line[0]
                ranges = line[1].split(" or ")
                fields.append(Field(rule_name, ranges))

            elif read_state == ReadState.YOUR_TICKET:
                if len(line) == 0:
                    read_state = ReadState.OTHER_TICKET
                    continue
                elif line != "your ticket:":
                    your_ticket = [int(value) for value in line.split(",")]

            elif read_state == ReadState.OTHER_TICKET:
                if line != "nearby tickets:":
                    other_tickets.append([int(value) for value in line.split(",")])

    error = 0

    for ticket in other_tickets:
        for number in ticket:
            valid = False
            for field in fields:
                if field.validate_number(number):
                    valid = True

            if not valid:
                error += number

    print(error)
