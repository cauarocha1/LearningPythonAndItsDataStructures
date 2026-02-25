# check if set is superset
set_a = {1, 2, 3}
set_b = {4, 1, 2, 5, 6, 3}

results = set_a.issuperset(set_b)  # False
print(results)

results = set_b.issuperset(set_a)  # True
print(results)
