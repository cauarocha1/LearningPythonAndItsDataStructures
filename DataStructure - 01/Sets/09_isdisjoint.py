# check if sets are disjoint
set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8, 9}
set_c = {1, 0}

results = set_a.isdisjoint(set_b)  # True
print(results)

results = set_a.isdisjoint(set_c)  # False
print(results)
