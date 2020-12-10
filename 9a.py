LENGTH = 25

if __name__ == "__main__":
    with open("9a.txt", "r") as f:
        data = [int(value) for value in f.read().splitlines()]

    for pointer in range(LENGTH, len(data)):
        valid = False
        for i in range(pointer - LENGTH, pointer):
            for j in range(pointer - LENGTH, pointer):
                if data[i] != data[j] and data[i] + data[j] == data[pointer]:
                    valid = True
        if not valid:
            print(data[pointer])
            break
