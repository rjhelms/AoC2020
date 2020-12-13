if __name__ == "__main__":
    with open("13a.txt", "r") as f:
        data = f.read().splitlines()
        time = int(data[0])
        routes = data[1].split(",")

    best_time = 999999
    best_route = 0
    for route in routes:
        if route == "x":
            continue

        remaining = int(route) - (time % int(route))
        if remaining < best_time:
            best_time = remaining
            best_route = int(route)

    print(best_time * best_route)
