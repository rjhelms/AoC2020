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

    contains_gold = False

    # else check each bag inside
    for content in bags[color]:

        # if the bag is gold, we're done
        if content[0] == "shiny gold":
            contains_gold = True
            break

        # otherwise, check the contents of that bag
        elif check_bag(content[0], level + 1) == True:
            contains_gold = True
            break

    log_level(color + ": " + str(contains_gold), level)
    dict_checked[color] = contains_gold
    return contains_gold


if __name__ == "__main__":

    with open("7a.txt", "r") as f:
        data = f.read().splitlines()
        for line in data:
            split = line[:-1].split("contain")
            bag = split[0].split(" bag")[0]
            contents = []
            if split[1] != " no other bags":
                contents_string = split[1][1:].split(", ")
                for rule in contents_string:
                    number = int(rule.split(" bag")[0].split(" ")[0])
                    color = (
                        rule.split(" bag")[0].split(" ")[1]
                        + " "
                        + rule.split(" bag")[0].split(" ")[2]
                    )
                    contents.append([color, number])

            bags[bag] = contents

    for bag in bags:
        check_bag(bag, 0)

    count = 0
    for bag in dict_checked:
        if dict_checked[bag]:
            count += 1
    print(count)
