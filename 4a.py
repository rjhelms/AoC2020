if __name__ == "__main__":
    passports = []
    with open("4a.txt", "r") as f:
        data = f.read().splitlines()
        passport = {}

        for line in data:
            if len(line) > 0:
                entries = line.split(" ")
                for entry in entries:
                    pair = entry.split(":")
                    passport[pair[0]] = pair[1]
            else:
                passports.append(passport)
                passport = {}

    valid_count = 0

    for passport in passports:
        if "cid" in passport:
            del passport["cid"]
        if len(passport) == 7:
            valid_count += 1

    print(valid_count)