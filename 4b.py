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
        valid = True
        if "byr" in passport:
            if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
                valid = False
        else:
            valid = False

        if "iyr" in passport:
            if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
                valid = False
        else:
            valid = False

        if "eyr" in passport:
            if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
                valid = False
        else:
            valid = False

        if "hgt" in passport:
            try:
                height = int(passport["hgt"][:-2])
                if passport["hgt"][-2:] == "in":
                    if height < 59 or height > 76:
                        valid = False
                elif passport["hgt"][-2:] == "cm":
                    if height < 150 or height > 193:
                        valid = False
                else:
                    valid = False
            except:
                valid = False
        else:
            valid = False

        if "hcl" in passport:
            if passport["hcl"][0] == "#":
                for i in range(1, 6):
                    if passport["hcl"][i] not in [
                        "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9",
                        "a",
                        "b",
                        "c",
                        "d",
                        "e",
                        "f",
                    ]:
                        valid = False
            else:
                valid = False
        else:
            valid = False

        if "ecl" in passport:
            if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
        else:
            valid = False

        if "pid" in passport:
            if len(passport["pid"]) == 9:
                pass
            else:
                valid = False
        else:
            valid = False

        if valid:
            valid_count += 1

    print(valid_count)
