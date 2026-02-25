# copy dictionary
contacts = {"guilherme@gmail.com": {"name": "Guilherme", "phone": "3333-2221"}}

copy_dict = contacts.copy()
copy_dict["guilherme@gmail.com"] = {"name": "Gui"}

print(contacts["guilherme@gmail.com"])  # {"name": "Guilherme", "phone": "3333-2221"}

print(copy_dict["guilherme@gmail.com"])  # {"name": "Gui"}
