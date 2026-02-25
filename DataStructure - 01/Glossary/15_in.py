# check if key is in dictionary
contacts = {
    "guilherme@gmail.com": {"name": "Guilherme", "phone": "3333-2221"},
    "giovanna@gmail.com": {"name": "Giovanna", "phone": "3443-2121"},
    "chappie@gmail.com": {"name": "Chappie", "phone": "3344-9871"},
    "melaine@gmail.com": {"name": "Melaine", "phone": "3333-7766"},
}

result = "guilherme@gmail.com" in contacts  # True
print(result)

result = "megui@gmail.com" in contacts  # False
print(result)

result = "age" in contacts["guilherme@gmail.com"]  # False
print(result)

result = "phone" in contacts["giovanna@gmail.com"]  # True
print(result)
