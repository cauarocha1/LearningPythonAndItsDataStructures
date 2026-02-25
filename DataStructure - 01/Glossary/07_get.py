# get method
contacts = {"guilherme@gmail.com": {"name": "Guilherme", "phone": "3333-2221"}}

# contacts["key"]  # KeyError

result = contacts.get("key")  # None
print(result)

result = contacts.get("key", {})  # {}
print(result)

result = contacts.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"name": "Guilherme", "phone": "3333-2221"}
print(result)
