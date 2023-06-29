import os

def calculate_root(operation, monkeys):
    if operation.isdigit():
        return int(operation)

    monkey_name, operator, job = operation.split(" ")
    monkey_name = calculate_root(monkeys[monkey_name], monkeys)
    job = calculate_root(monkeys[job], monkeys)

    if operator == "+":
        return monkey_name + job
    elif operator == "-":
        return monkey_name - job
    elif operator == "*":
        return monkey_name * job
    else:
        return monkey_name // job


file_path = os.path.join(os.path.dirname('__file__'), "day21.in")

monkeys: dict[str, str] = {} #maps monkey name to operations (both are strings)

with open(file_path) as file:
    for line in file:
        name, operation = line.strip().split(": ")
        monkeys[name] = operation

print("Root Number :", calculate_root(monkeys["root"], monkeys))


