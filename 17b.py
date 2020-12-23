import time

STAY_ACTIVE = [2, 3]
BECOME_ACTIVE = [3]

cubes = {}
new_cubes = {}


def get_cube(position):
    """
    Returns the cube at this position if it exists, otherwise instantiates one.
    """
    if position in cubes:
        return cubes[position]

    new_cube = Cube(position, False, new_cubes)
    return new_cube


class Cube:
    def __init__(self, position, state, destination):
        self.state = state
        self.position = position
        destination[self.position] = self

        self.new_state = False

    # tick - get the new status
    def tick(self) -> int:
        neighbours = 0
        for x in range(self.position[0] - 1, self.position[0] + 2):
            for y in range(self.position[1] - 1, self.position[1] + 2):
                for z in range(self.position[2] - 1, self.position[2] + 2):
                    for w in range(self.position[3] - 1, self.position[3] + 2):
                        check_position = (x, y, z, w)
                        if (
                            check_position != self.position
                            and get_cube(check_position).state
                        ):
                            neighbours += 1

        if self.state:
            self.new_state = True
            if neighbours not in STAY_ACTIVE:
                self.new_state = False
        else:
            self.new_state = False
            if neighbours in BECOME_ACTIVE:
                self.new_state = True

        if self.state == self.new_state:
            return 0
        return 1

    # tock - apply the change
    def tock(self) -> int:
        self.state = self.new_state
        if self.state:
            return 1
        return 0


if __name__ == "__main__":
    start_time = time.time()
    with open("17a.txt", "r") as f:
        data = f.read().splitlines()

    # build initial list of cubes
    init_x = len(data[0])
    init_y = len(data)
    for x in range(init_x):
        for y in range(init_y):
            if data[y][x] == "#":
                Cube((x, y, 0, 0), True, cubes)

    iteration = 0

    # run 6 cycles

    while iteration < 6:
        iteration += 1
        active = 0
        old_change = 0

        # cubes can get instantiated while checking - so repeatedly check until change settles down
        old_changed = 0
        while True:
            change = 0
            for cube in cubes:
                change += cubes[cube].tick()

            cubes.update(new_cubes)
            new_cubes = {}

            if change == old_change:
                break
            old_change = change

        for cube in cubes:
            active += cubes[cube].tock()

        print(f"Iteration {iteration}: {change} changed, {active} active")

    print(f"--- {time.time() - start_time} seconds ---")
