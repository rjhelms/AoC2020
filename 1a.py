num_list = []
with open("1a.txt", "r") as f:
    for x in f:
        num_list.append(int(x))

num_list.sort()

for x in num_list:
    for y in reversed(num_list):
        if y < x:
            break

        candidate = x + y
        if candidate < 2020:
            break
        if candidate == 2020:
            print(x, y)
            print(x * y)
