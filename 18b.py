homework = []


def evaluate(expression):

    result = 0
    added_list = []

    # do additions first
    operation = "+"

    for item in expression:
        if item == "*":
            added_list.append(result)
            added_list.append("*")
            result = 0
        elif item == "+":
            operation = "+"
        elif type(item) == int:
            if operation == "+":
                result += item
            else:
                result *= item
        else:
            if operation == "+":
                result += evaluate(item)
            else:
                result *= evaluate(item)
    added_list.append(result)

    # then multiplication

    result = 0
    operation = "+"
    for item in added_list:
        if type(item) == str:
            operation = item
        elif type(item) == int:
            if operation == "+":
                result += item
            else:
                result *= item
        else:
            if operation == "+":
                result += evaluate(item)
            else:
                result *= evaluate(item)

    return result


if __name__ == "__main__":
    with open("18a.txt", "r") as f:
        data = f.read().splitlines()

    for line in data:
        stack = [[]]
        stack_depth = 0
        for char in line:
            if char == " ":
                continue
            if char == "+" or char == "*":
                stack[stack_depth].append(char)
            elif char == "(":
                stack_depth += 1
                stack.append([])
            elif char == ")":
                stack[stack_depth - 1].append(stack[stack_depth])
                stack.remove(stack[stack_depth])
                stack_depth -= 1
            else:
                stack[stack_depth].append(int(char))
        homework.append(stack[0])

    sum = 0
    for line in homework:
        sum += evaluate(line)

    print(sum)
