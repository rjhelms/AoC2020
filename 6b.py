from collections import Counter

if __name__ == "__main__":
    with open("6a.txt", "r") as f:
        data = f.read().splitlines()
        teams = []
        entry = ""
        participants = 0
        for line in data:
            if len(line) > 0:
                participants += 1
                entry += line
            else:
                teams.append({"entry": entry, "participants": participants})
                entry = ""
                participants = 0

        # make sure to catch the last entry
        teams.append({"entry": entry, "participants": participants})

    count = 0
    for team in teams:
        for answer_count in Counter(team["entry"]).values():
            if answer_count == team["participants"]:
                count += 1

    print(count)
