class Password:
    min_count = None
    max_count = None
    letter = None
    password = None

    def valid(self):
        occurance = self.password.count(self.letter)
        if occurance >= self.min_count and occurance <= self.max_count:
            return True
        else:
            return False


passwords = []
with open("2a.txt", "r") as f:
    for row in f:
        new_password = Password()
        split_row = row.split(" ")
        lengths = split_row[0].split("-")
        new_password.min_count = int(lengths[0])
        new_password.max_count = int(lengths[1])
        new_password.letter = split_row[1][0]
        new_password.password = split_row[-1][:-1]
        passwords.append(new_password)

valid_count = 0

for candidate in passwords:
    if candidate.valid():
        valid_count += 1

print(valid_count)