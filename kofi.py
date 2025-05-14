amount=float(input("Enter amount: "))
if amount<100:
    print("Telecom Charge: GH¢ 0.00 ",end="  ")
    print("E-levy: GH¢0.00")
elif 100<=amount<101:
    print("Telecom Charge: GH¢ 0.00 ",end="  ")
    print("E-levy: GH¢1.00")