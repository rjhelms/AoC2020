DEFAULT_ONE_MASK = 0
DEFAULT_FLOAT_MASK = 0


def twiddle(memory, location, value, float_mask):
    if float_mask == "":
        memory[location] = value
        return
    if float_mask[0] == "1":
        one_location = location | 1 << (len(float_mask) - 1)
        zero_location = location & ~(1 << (len(float_mask) - 1))
        twiddle(memory, one_location, value, float_mask[1:])
        twiddle(memory, zero_location, value, float_mask[1:])
        pass
    else:
        twiddle(memory, location, value, float_mask[1:])


def set_masks(new_mask: str) -> None:
    one_mask = DEFAULT_ONE_MASK
    float_mask = DEFAULT_FLOAT_MASK

    for i in range(len(new_mask)):
        offset = len(new_mask) - i - 1
        if new_mask[i] == "1":
            one_mask += 1 << offset
        elif new_mask[i] == "X":
            float_mask += 1 << offset
    return (one_mask, bin(float_mask)[2:])


if __name__ == "__main__":
    memory = {}
    one_mask = DEFAULT_ONE_MASK
    float_mask = bin(DEFAULT_FLOAT_MASK)[2:]
    with open("14a.txt", "r") as f:
        data = f.read().splitlines()

    for line in data:
        line = line.split(" = ")
        if line[0] == "mask":
            one_mask, float_mask = set_masks(line[1])
            continue
        else:
            location = int(line[0].strip("me[]"))
            location = location | one_mask
            value = int(line[1])
            twiddle(memory, location, value, float_mask)

    sum = 0
    for location in memory:
        sum += memory[location]
    print(sum)
