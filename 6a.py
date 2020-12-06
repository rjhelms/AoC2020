from collections import Counter

if __name__ == "__main__":
    with open("6a.txt", "r") as f:
        data = f.read().splitlines()
        teams = []
        entry = ""
        for line in data:
            if len(line) > 0:
                entry += line
            else:
                teams.append(entry)
                entry = ""

        # make sure to catch the last entry
        teams.append(entry)

    count = 0
    for team in teams:
        count += len(Counter(teams).keys())

    print(count)
