# AND = to be True, all need to be True
# OR = to be True, just one need to be True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

balance = 1000
withdraw = 250
limit = 200
special_account = True

exp = balance >= withdraw and withdraw <= limit or special_account and balance >= withdraw
print(exp)

exp_2 = (balance >= withdraw and withdraw <= limit) or (special_account and balance >= withdraw)
print(exp_2)

normal_account_with_enough_balance = balance >= withdraw and withdraw <= limit
special_account_with_enough_balance = special_account and balance >= withdraw

exp_3 = normal_account_with_enough_balance or special_account_with_enough_balance
print(exp_3)