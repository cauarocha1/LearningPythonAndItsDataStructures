#enumerate: enumerates the objects into a list
cars = {"gol", "celta", "palio"}

for carro in cars:
    print(carro)

for index, carro in enumerate(cars):
    print(f"{index}: {carro}")
