# first class objects
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test(a, b):
    return 3*a + 2*b


def display_result(a, b, function):
    result = function(a, b)
    print(f"The result of the operation is = {result}")


display_result(10, 10, add)  # The result of the operation is = 20
display_result(10, 10, subtract)  # The result of the operation is = 0
display_result(10, 10, test)  # The result of the operation is = 50
