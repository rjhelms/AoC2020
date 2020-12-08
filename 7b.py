dict_checked = {}
bags = {}


def log_level(message, level):
    for i in range(level):
        print("-", end="")
    print(message)


def check_bag(color, level):

    log_level("Checking " + color, level)

    # check if it's in the dictionary of things already checked

    if color in dict_checked:
        log_level("Already checked: " + str(dict_checked[color]), level)
        return dict_checked[color]

    number_contained = 0

    # else check each bag inside

    for content in bags[color]:
        number_contained += content[1]
        number_contained += check_bag(content[0], level + 1) * content[1]

    log_level(color + ": " + str(number_contained), level)
    dict_checked[color] = number_contained
    return number_contained


if __name__ == "__main__":

    with open("7a.txt", "r") as f:
        data = (
            f.read()
            .replace(" contain no other", "")
            .replace(" bags", "")
            .replace(" bag", "")
            .replace(" contain ", ",")
            .replace(".", "")
            .splitlines()
        )
        for line in data:
            split = line.split(",")
            bag = split[0]
            contents = []
            if len(split) > 1:
                for i in split[1:]:
                    i = i.strip()
                    number = int(i[0])
                    color = i[2:]
                    contents.append([color, number])

            bags[bag] = contents

    for bag in bags:
        check_bag(bag, 0)

    print(dict_checked["shiny gold"])
