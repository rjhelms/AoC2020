DATA = []
WIDTH = 0


def hits(x, y):
    x_pos = 0
    y_pos = 0
    hits = 0
    while y_pos < len(DATA):
        print(x_pos, y_pos)
        if DATA[y_pos][x_pos] == "#":
            hits += 1
        x_pos += x
        x_pos = x_pos % WIDTH
        y_pos += y
    return hits


with open("3a.txt", "r") as f:
    DATA = f.read().splitlines()
    WIDTH = len(DATA[0])

if __name__ == "__main__":
    print(hits(1, 1) * hits(3, 1) * hits(5, 1) * hits(7, 1) * hits(1, 2))
