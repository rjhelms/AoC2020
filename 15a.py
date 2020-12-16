memory = {}

MAX_TURNS = 2020

if __name__ == "__main__":
    with open("15a.txt", "r") as f:
        data = [int(value) for value in f.read().split(",")]

    turn = 0
    last_said = data[0]

    while turn < MAX_TURNS:
        if turn < len(data):
            say = data[turn]
        else:
            if last_said in memory:
                say = turn - memory[last_said]
            else:
                say = 0
        memory[last_said] = turn
        last_said = say

        turn += 1

    print(say)
