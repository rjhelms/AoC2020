if __name__ == "__main__":
    with open("5a.txt", "r") as f:
        data = f.read().splitlines()

        values = []
        for line in data:
            value = 0
            for char in line:
                value <<= 1
                if char == "B" or char == "R":
                    value += 1
            values.append(value)

    values.sort()
    print(values[-1])
