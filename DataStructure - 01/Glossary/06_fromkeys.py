# fromkeys method
result = dict.fromkeys(["name", "phone"])  # {"name": None, "phone": None}
print(result)

result = dict.fromkeys(["name", "phone"], "empty")  # {"name": "empty", "phone": "empty"}
print(result)
