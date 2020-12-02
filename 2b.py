class Password:
    min_count = None
    max_count = None
    letter = None
    password = None

    def valid(self):
        occurance = 0
        if self.password[self.min_count - 1] == self.letter:
            occurance += 1
        if self.password[self.max_count - 1] == self.letter:
            occurance += 1
        if occurance == 1:
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
