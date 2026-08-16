customer_name = input("Enter your name : ")
invoice_amount = float(input("Enter your invoice amount : ")) 

if invoice_amount >= 10000:
    discount = 0.10
elif invoice_amount >= 5000:
    discount = 0.05
elif invoice_amount >= 2000:
    discount = 0.02
else:
    discount = 0

total_discount = invoice_amount * discount
total_after_discount = invoice_amount - total_discount 

print(f"Hello {customer_name} your after discount is {total_after_discount}")