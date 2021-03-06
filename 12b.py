if __name__ == "__main__":
    x = 0
    y = 0
    waypoint_x = 10
    waypoint_y = -1
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
            waypoint_y -= instruction[1]
        elif instruction[0] == "E":
            waypoint_x += instruction[1]
        elif instruction[0] == "S":
            waypoint_y += instruction[1]
        elif instruction[0] == "W":
            waypoint_x -= instruction[1]
        elif instruction[0] == "F":
            x += waypoint_x * instruction[1]
            y += waypoint_y * instruction[1]
        elif instruction[1] == 180:
            waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
        else:
            angle = instruction[1]
            if instruction[0] == "L":
                angle = 360 - angle
            if angle == 90:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
            elif angle == 270:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x

        print(
            instruction[0],
            instruction[1],
            "waypoint:",
            waypoint_x,
            waypoint_y,
            "position:",
            x,
            y,
        )

    print(abs(x) + abs(y))
