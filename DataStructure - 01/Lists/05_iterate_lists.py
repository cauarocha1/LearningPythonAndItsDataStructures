#enumerate: enumerates the objects into a list
cars = ["Onix", "Golf", "Tracker"]

for car in cars:
    print(car)


for index, car in enumerate(cars):
    print(f"{index}: {car}")