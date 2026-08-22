Employee_Name = input("Employee Name Here : ")
Salary = float(input("Salary here : "))
Years_of_service = float(input("Years of service here : "))

if Years_of_service > 10:
    bonus = 0.10
elif Years_of_service >= 5:
    bonus = 0.05
elif Years_of_service >= 2:
    bonus = 0.02
else:
    bonus = 0

bonus_amount = Salary * bonus
final_salary = Salary + bonus_amount
print(f"Final salary is {final_salary} and bonus for years earned was {bonus_amount}")
