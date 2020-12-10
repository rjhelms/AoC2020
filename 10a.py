if __name__ == "__main__":
    with open("10a.txt", "r") as f:
        data = [int(value) for value in f.read().splitlines()]
        data.sort()
    
    ones = 0
    threes = 0
    last = 0
    for val in data:
        if val - last == 1:
            ones += 1
        elif val - last == 3:
            threes += 1
        elif val - last > 3:
            print("illegal")
        last = val

    threes += 1 # for the final adapters

    print(ones, threes)
    print(ones * threes)