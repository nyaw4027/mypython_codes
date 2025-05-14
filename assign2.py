price = 12.50
item = input("What item are you buying? ")
print(f"Item: {item}")
print(f"Price: Ghs {price}")
cash_paid = float(input("How much cash are you paying? Ghs "))

print(f"Item: {item}")
balance = float(cash_paid - price )
print(f"Your new balance is: GH{balance}")