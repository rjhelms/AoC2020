if __name__ == "__main__":
    with open("13a.txt", "r") as f:
        data = f.read().splitlines()
        time = int(data[0])
        routes = data[1].split(",")

    offsets = []

    for route in routes:
        if route == "x":
            continue
        time = int(route) - routes.index(route)
        while time < 0:
            time += int(route)
        offsets.append([int(route), time])

    step = offsets[0][0]
    offsets = offsets[1:]
    offsets.sort(key=lambda x: x[1], reverse=True)

    iteration = 0
    time = step
    for offset in offsets:
        print("New step", step)
        while True:
            iteration += 1
            time += step
            if ((time % offset[0])) == offset[1]:
                print("Found", offset[0], "at", time)
                step = step * offset[0]
                break
        print("Iteration", iteration)
        print()

    print(time)
