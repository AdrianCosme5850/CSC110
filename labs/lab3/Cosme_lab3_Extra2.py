# Adrian Cosme-Halverson
# 08 JUL 23
# A program that sums the digits in a four digit number, I added input validation to the program to ensure that
# the user only uses four digit numbers

# input section
number = input("Please, enter a 4-digit number: ")

#input validation
if len(number) != 4:
    print('Please use a four digit number!')
    exit()
else:
   number = int(number)

if number < 1000 or number > 9999:
    print('Please use a four digit number!')
    exit()
# Operation section
digit1 = number//1000
digit2 = number%1000//100
digit3 = (number%100)//10
digit4 = number%10
sumFirstTwo = digit1 + digit2
sumSecondTwo = digit3 + digit4

# Output section

if sumFirstTwo == sumSecondTwo:
    print('The four digit number is ' + str(number) + '. The sum of the first two digits equals the sum of the last two digits')
else:
    print('The four digit number is ' + str(number) + '. The sum of the first two digits does not equal the sum of the last two digits.')

# Written report
# Just changed the program slightly to add the first two digits into one variable, and then add the second two
# in another variable. They are then compared and if they equal each other, a message is printed saying so.