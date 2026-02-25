# update method
contacts = {"guilherme@gmail.com": {"name": "Guilherme", "phone": "3333-2221"}}

contacts.update({"guilherme@gmail.com": {"name": "Gui"}})
print(contacts)  # {'guilherme@gmail.com': {'name': 'Gui'}}

contacts.update({"giovanna@gmail.com": {"name": "Giovanna", "phone": "3322-8181"}})
# {'guilherme@gmail.com': {'name': 'Gui'}, 'giovanna@gmail.com': {'name': 'Giovanna', 'phone': '3322-8181'}}
print(contacts)
