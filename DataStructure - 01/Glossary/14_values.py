# values method
contacts = {
    "guilherme@gmail.com": {"name": "Guilherme", "phone": "3333-2221"},
    "giovanna@gmail.com": {"name": "Giovanna", "phone": "3443-2121"},
    "chappie@gmail.com": {"name": "Chappie", "phone": "3344-9871"},
    "melaine@gmail.com": {"name": "Melaine", "phone": "3333-7766"},
}

result = (
    contacts.values()
)  # dict_values([{'name': 'Guilherme', 'phone': '3333-2221'}, {'name': 'Giovanna', 'phone': '3443-2121'}, {'name': 'Chappie', 'phone': '3344-9871'}, {'name': 'Melaine', 'phone': '3333-7766'}])  # noqa
print(result)
