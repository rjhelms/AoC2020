LENGTH = 25


def find_range(target):
    for i in range(0, len(data)):
        value = 0
        for j in range(i, len(data)):
            value += data[j]
            if value == target:
                return [i, j + 1]
            if value > target: 
                break


if __name__ == "__main__":
    with open("9a.txt", "r") as f:
        data = [int(value) for value in f.read().splitlines()]

    for pointer in range(LENGTH, len(data)):
        valid = False
        for i in range(pointer - LENGTH, pointer):
            for j in range(pointer - LENGTH, pointer):
                if data[i] != data[j] and data[i] + data[j] == data[pointer]:
                    valid = True
        if not valid:
            break

    target = data[pointer]
    target_range = find_range(target)
    range_min = float("inf")
    range_max = 0
    for i in range(target_range[0], target_range[1]):
        if data[i] > range_max:
            range_max = data[i]
        if data[i] < range_min:
            range_min = data[i]

    print(range_min + range_max)
