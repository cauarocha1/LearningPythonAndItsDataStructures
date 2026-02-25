# function return
def calculate_total(numbers):
    return sum(numbers)


def return_predecessor_and_successor(number):
    predecessor = number - 1
    successor = number + 1

    return predecessor, successor


print(calculate_total([10, 20, 34]))  # 64
print(return_predecessor_and_successor(10))  # (9, 11)
