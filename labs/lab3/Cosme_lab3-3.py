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
sumTotal = digit1 + digit2 + digit3 + digit4

# Output section
print("The number was", str(number) + ", the final sum of all digits is",
      str(sumTotal) + ".")

# Written report
# I wanted to test how to find the length of a string, so I worked it into the input validation.
# It now checks to see if the string is four characters long, and if it is converts it to an integer.
# After a bit of testing I realized that an edge case could be a user putting in 0034, and still receiving
# a result. I put in an extra if statement to deal with the edge case.