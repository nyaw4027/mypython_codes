# PROGRAM to find if a numberis odd or even
# <= 100 - No elevy
# <=101 - ghs 2 elevy charges
# <= 100- No telecom charges 
# <= ghs 1 no charges

# amount=float(input("Enter amount: "))
# if amount<100:
#     print("Telecom Charge: GH¢ 0.00 ",end="  ")
#     print("E-levy: GH¢0.00")
# elif 100<=amount<101:
#     print("Telecom Charge: GH¢ 0.00 ",end="  ")
#     print("E-levy:GH¢1.00")

#     #program to find whehter a number is odd or even.
# while True:
#     number=int(input("Enter a number: "))
#     if number%2==0:
#         print("The number is even.")
#     else:
#         print("The number is odd.")
#     response=input("Enter 0 to terminate, 1 to reiterate.")
#     if response=="0":
#         break

amount = float(input("Enter amount: "))
if amount <= 100.00:
    print(f"Amount sent {amount}.00")
elif amount >= 101:
    print(f"Amount sent: {amount}.00")
    elevy_Charges = 2
    telecosCharge = 1
    allCharges = int(elevy_Charges + telecosCharge) 
    totalsent = int(amount + allCharges)
    print(f"Elevy Charges: {str (elevy_Charges)}.00")
    print(f"Telecos Charges {str (telecosCharge)}.00")
    print(f"Total Charges:  { str (allCharges)}.00")
    print(f"Total payment: {str (totalsent)}.00")

