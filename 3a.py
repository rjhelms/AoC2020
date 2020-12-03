X = 3
Y = 1

if __name__ == "__main__":
    x_pos = 0
    y_pos = 0
    hits = 0
    with open("3a.txt", "r") as f:
        data = f.read().splitlines()
        print(data)
        width = len(data[0])
        while y_pos < len(data):
            print(x_pos, y_pos)
            if data[y_pos][x_pos] == "#":
                hits += 1
            x_pos += X
            x_pos = x_pos % width
            y_pos += Y
    print(hits)
