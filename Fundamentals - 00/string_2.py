name = "Caua"
age = "18"
position = "Student"
language = "Python"
balance = 42.543

data = {"name": "Caua", "age": "18"}

#print("Name: %s Age: %d" % (name, age))

print("Name: {} Age: {}" .format(name, age))

print("Name: {1} Age: {0}" .format(age, name))
print("Name: {1} Age: {0} Name: {1} {1}" .format(age, name))

print("Name: {name} Age: {age}" .format(name=name, age=age))
print("Name: {name} Age: {age}" .format(name=name, age=age))
print("Name: {name} Age: {age}" .format(**data))

print(f"Name: {name} Age: {age}")
print(f"Name: {name} Age: {age} Balance: {balance:.2f}")
print(f"Name: {name} Age: {age} Balance: {balance:10.2f}")