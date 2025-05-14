# PROGRAM to find if a numberis odd or even
# <= 100 - No elevy
# <=101 - ghs 2 elevy charges
# <= 100- No telecom charges 
# <= ghs 1 no charges

def check_number(num):
    # Check if the number is odd or even
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    
    # Check the charges based on the number
    if num <= 100:
        print("No charge.")
    elif num == 101:
        print("GHS 2 charge applies.")
    else:
        print("No charges for numbers greater than 101.")

# Input number from the user
try:
    num = float(input("Enter a number: "))
    check_number(num)
except ValueError:
    print("Please enter a valid integer.")
