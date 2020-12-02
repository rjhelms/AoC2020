num_list = []
with open("1a.txt", "r") as f:
    for x in f:
        num_list.append(int(x))

num_list.sort()

for x in num_list:
    for y in num_list:
        for z in num_list:
            candidate = x + y + z
            if candidate == 2020:
                print (x, y, z)
                print (x * y * z)
                exit()
