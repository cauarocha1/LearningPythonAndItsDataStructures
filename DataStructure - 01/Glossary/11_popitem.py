# popitem method
contacts = {"guilherme@gmail.com": {"name": "Guilherme", "phone": "3333-2221"}}

result = contacts.popitem()  # ('guilherme@gmail.com', {'name': 'Guilherme', 'phone': '3333-2221'})
print(result)

# contacts.popitem()  # KeyError
