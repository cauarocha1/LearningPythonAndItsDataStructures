# delete from dictionary
contacts = {
    "guilherme@gmail.com": {"name": "Guilherme", "phone": "3333-2221"},
    "giovanna@gmail.com": {"name": "Giovanna", "phone": "3443-2121"},
    "chappie@gmail.com": {"name": "Chappie", "phone": "3344-9871"},
    "melaine@gmail.com": {"name": "Melaine", "phone": "3333-7766"},
}

del contacts["guilherme@gmail.com"]["phone"]
del contacts["chappie@gmail.com"]

# {'guilherme@gmail.com': {'name': 'Guilherme'}, 'giovanna@gmail.com': {'name': 'Giovanna', 'phone': '3443-2121'}, 'melaine@gmail.com': {'name': 'Melaine', 'phone': '3333-7766'}}  # noqa
print(contacts)
