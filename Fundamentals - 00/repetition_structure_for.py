text = input("Insert your text: ")
VOGALS = "AEIOU"

#example using a iterable
for letter in text:
    if letter.upper() in VOGALS:
        print(letter, end="")
else:
    print() #line break
    print("final of loop")


#example using function built-in range
for number in range(0, 61, 6):
    print(number, end=" ")

