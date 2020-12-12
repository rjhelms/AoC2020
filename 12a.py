if __name__ == "__main__":
    x = 0
    y = 0
    angle = 0
    instructions = []
    with open("12a.txt", "r") as f:
        data = f.read().splitlines()
        for line in data:
            action = line[0]
            distance = int(line[1:])
            instruction = [action, distance]
            instructions.append(instruction)

    for instruction in instructions:
        if instruction[0] == "N":
            y -= instruction[1]
        elif instruction[0] == "E":
            x += instruction[1]
        elif instruction[0] == "S":
            y += instruction[1]
        elif instruction[0] == "W":
            x -= instruction[1]
        elif instruction[0] == "L":
            angle -= instruction[1]
        elif instruction[0] == "R":
            angle += instruction[1]
        elif instruction[0] == "F":
            if angle == 0:
                x += instruction[1]
            if angle == 90:
                y += instruction[1]
            if angle == 180:
                x -= instruction[1]
            if angle == 270:
                y -= instruction[1]
        if angle < 0:
            angle += 360
        if angle >= 360:
            angle -= 360
        print(instruction[0], instruction[1], angle, x, y)

    print(abs(x) + abs(y))
