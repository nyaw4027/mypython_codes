def vote (age:int):
    if age <= 18:
     return("You are eligible to vote. ")
    else:
       return("You are not eligible to vote.")
age =int(input("How old are you? "))
print(vote(age))



def even_odd(num):
   if num % 2==0:
      
        print("The number is even")
   else:
      
    print("The number is odd")
num = int(input("Enter any number: "))
even_odd(num)

   