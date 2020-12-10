steps = {}


def check_step(value, target, count):

    if value == target:
        return count + 1

    for candidate in steps[value]:
        count = check_step(candidate, target, count)

    return count


if __name__ == "__main__":

    with open("10a.txt", "r") as f:
        data = [int(value) for value in f.read().splitlines()]
        data.sort()
    data.append(data[-1] + 3)
    data.append(0)
    data.sort(reverse=True)

    for val in data:
        val_steps = []
        candidates = [val - 1, val - 2, val - 3]
        for candidate in candidates:
            if candidate in data:
                val_steps.append(candidate)
        steps[val] = val_steps

    # find gaps of three - there is only one through that ndde

    breaks = []
    for i in data:
        if i - 1 not in data and i - 2 not in data:
            breaks.append(i)

    # get number of possible paths between each break
    # multiply for total paths from start to end

    count = 1
    for i in range(1, len(breaks)):
        count *= check_step(breaks[i - 1], breaks[i], 0)

    print(count)
