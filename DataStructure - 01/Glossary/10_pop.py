# pop method
contacts = {"guilherme@gmail.com": {"name": "Guilherme", "phone": "3333-2221"}}

result = contacts.pop("guilherme@gmail.com")  # {'name': 'Guilherme', 'phone': '3333-2221'}
print(result)

result = contacts.pop("guilherme@gmail.com", {})  # {}
print(result)
