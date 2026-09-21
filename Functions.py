employees = [
    {"name": "Ahmed", "salary": 5000},
    {"name": "Ali", "salary": 7000},
    {"name": "Omar", "salary": 9000}
]

for employee in employees:
    if employee["salary"] >= 8000:
        bonus = 0.10
    elif employee["salary"] >= 6000:
        bonus = 0.05
    else:
        bonus = 0
    total_bonus = employee["salary"] * bonus
    print(f"{employee['name']} - Bonus: {total_bonus}")