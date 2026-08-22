salary = [5000, 5000, 7000, 9000]

for salaries in salary:
    if salaries >= 8000:
        bonus = 0.10
    elif salaries >= 5000:
        bonus = 0.10
    else:
        bonus = 0

    Adding_bonus = salaries * bonus
    Final_after_adding_bonus = Adding_bonus + salaries
    print(f"Salary: {salaries} - Final:    {Final_after_adding_bonus}")