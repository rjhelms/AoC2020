from enum import Enum


class Field:
    def __init__(self, name, ranges):
        self.name = name
        self.ranges = []
        for range in ranges:
            self.ranges.append([int(value) for value in range.split("-")])
        self.candidate_indices = []

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

    # parse the data file

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

    # validate the nearby tickets

    invalid_tickets = []
    for ticket in other_tickets:
        for number in ticket:
            valid = False
            for field in fields:
                if field.validate_number(number):
                    valid = True

            if not valid:
                invalid_tickets.append(ticket)

    # discard invalid nearby tickets

    other_tickets = [
        ticket for ticket in other_tickets if ticket not in invalid_tickets
    ]

    # for each field, determine indices where all nearby tickets are valid
    # there should be at least one field that only has one possible index

    for i in range(len(your_ticket)):
        for field in fields:
            field.candidate_indices.append(i)
        for ticket in other_tickets:
            for field in fields:
                if not field.validate_number(ticket[i]):
                    field.candidate_indices.remove(i)

    confirmed_fields = []

    # iterate through fields repeatedly, until every field index is confirmed

    while len(fields) > 0:
        for field in fields:
            if len(field.candidate_indices) == 1:

                # if a field only has one possible index, move it to another list...
                confirmed_fields.append(field)

                # ... and remove that index from all other fields
                for remove_field in fields:
                    if remove_field is not field:
                        if field.candidate_indices[0] in remove_field.candidate_indices:
                            remove_field.candidate_indices.remove(
                                field.candidate_indices[0]
                            )

        fields = [field for field in fields if field not in confirmed_fields]

    result = 1
    for field in confirmed_fields:
        if field.name.split(" ")[0] == "departure":
            result *= your_ticket[field.candidate_indices[0]]

    print(result)
