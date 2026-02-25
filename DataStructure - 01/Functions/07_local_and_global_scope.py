# local and global scope
salary = 2000


def salary_bonus(bonus):
    global salary
    salary += bonus
    return salary


salary_with_bonus = salary_bonus(500)
print(salary_with_bonus)  # 2500