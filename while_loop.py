salaries = [3000, 0, 6000, 9000, 0, 12000]

for salary in salaries:
        if salary == 0:
                continue
        elif salary >= 10000:
                bonus = 0.10
        elif salary >= 5000:
                bonus = 0.05
        else:
            bonus = 0
        final_bonus = salary * bonus
        salary_after_bonus = (final_bonus + salary)

        print(f"Salary: {salary} -- Final: {salary_after_bonus}")