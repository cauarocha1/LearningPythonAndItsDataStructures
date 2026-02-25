# discard element from set
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numbers)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numbers.discard(1)
numbers.discard(45)

print(numbers)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
