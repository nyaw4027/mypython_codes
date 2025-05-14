price = 12.50
item = input("What item are you buying? ")
print(f"Item: {item}")
print(f"Price: Ghs {price:.2f}")
cash_paid = float(input("How much cash are you paying? Ghs "))
print(f"Item: {item}")
print(f"You paid: Ghs {cash_paid:}")
if cash_paid > price:
    balance = cash_paid - price
    print(f"Your balance is: Ghs {balance:.2f}")
else:
    print("Insufficient amount. Please pay more.")