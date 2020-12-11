boat = []
WIDTH = 0
HEIGHT = 0


class Space:
    occupied: bool = False
    changed: bool = False
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def calculate_change(self) -> bool:
        self.changed = False
        return self.changed

    def apply_change(self) -> None:
        return

    def __str__(self) -> str:
        return "."


class Seat(Space):
    new_occupied: bool = False

    def __str__(self) -> str:
        if self.occupied:
            return "#"
        else:
            return "L"

    def look(self, vector) -> bool:
        look_x = self.x
        look_y = self.y

        while True:
            look_x += vector[0]
            look_y += vector[1]
            if look_x < 0 or look_y < 0 or look_x >= WIDTH or look_y >= HEIGHT:
                return False
            if isinstance(boat[look_y][look_x], Seat):
                return boat[look_y][look_x].occupied
        # should never get here
        return False

    def calculate_change(self) -> bool:
        neighbours = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                vector = [x, y]
                if vector != [0, 0]:
                    if self.look(vector):
                        neighbours += 1

        if self.occupied == False and neighbours == 0:
            self.new_occupied = True
        if self.occupied == True and neighbours >= 5:
            self.new_occupied = False
        self.changed = self.occupied != self.new_occupied
        return self.changed

    def apply_change(self) -> None:
        self.occupied = self.new_occupied


if __name__ == "__main__":
    total_seats = 0
    with open("11a.txt", "r") as f:
        data = f.read().splitlines()
        WIDTH = len(data[0])
        HEIGHT = len(data)
        for y in range(len(data)):
            row = []
            for x in range(len(data[0])):
                char = data[y][x]
                if char == ".":
                    space = Space(x, y)
                else:
                    space = Seat(x, y)
                    total_seats += 1
                row.append(space)
            boat.append(row)

        changed_seats = total_seats
        iteration = 0
        while changed_seats > 0:
            iteration += 1

            changed_seats = 0
            for row in boat:
                for space in row:
                    if space.calculate_change():
                        changed_seats += 1
            occupied = 0
            for row in boat:
                for space in row:
                    space.apply_change()
                    if space.occupied:
                        occupied += 1

        print("Iteration", iteration)
        print("Occupied:", occupied)
