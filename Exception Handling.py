try:
    invoice_amount = float(input("Enter Invoice Amount: "))
    number_of_items = int(input("Enter Item's number: "))
    average_cost = invoice_amount / number_of_items
    print(average_cost)

except ValueError:
    print("Enter Amount only!")

except ZeroDivisionError:
    print("cannot divide with less than one!")

finally:
    print("Calculation finished") 