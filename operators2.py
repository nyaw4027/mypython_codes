# even_number = 5
# answer = even_number/2
# print(answer)



# region = 'Takoradi'
# if (region == 'Accra'):
#     tax = 0.75
# elif(region == 'Takoradi'):
#     tax = 0.55
# else: 
#     tax = 0.50
# print(tax)

number =int(input('Any number: ')) 
odd_even = number % 2
if odd_even == 0:
    answer = 'even'
else:
    answer = 'odd'
print(answer)

