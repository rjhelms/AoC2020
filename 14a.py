DEFAULT_ONE_MASK = 0
DEFAULT_ZERO_MASK = 0xFFFFFFFFF  # 36 bytes of ones


def set_masks(new_mask: str) -> None:
    one_mask = DEFAULT_ONE_MASK
    zero_mask = DEFAULT_ZERO_MASK

    for i in range(len(new_mask)):
        offset = len(new_mask) - i - 1
        if new_mask[i] == "1":
            one_mask += 1 << offset
        elif new_mask[i] == "0":
            zero_mask -= 1 << offset
    return (one_mask, zero_mask)


if __name__ == "__main__":
    memory = {}
    one_mask = DEFAULT_ONE_MASK
    zero_mask = DEFAULT_ZERO_MASK
    with open("14a.txt", "r") as f:
        data = f.read().splitlines()

    for line in data:
        line = line.split(" = ")
        if line[0] == "mask":
            one_mask, zero_mask = set_masks(line[1])
            continue
        else:
            location = int(line[0].strip("me[]"))
            value = int(line[1])
            masked_value = value | one_mask
            masked_value = masked_value & zero_mask
            memory[location] = masked_value

    sum = 0
    for location in memory:
        sum += memory[location]
    print(sum)
