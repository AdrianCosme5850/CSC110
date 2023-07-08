# Adrian Cosme-Halverson
# 08 JUL 23
# A program to calculate the sum of each individual number in a three digit number, I added 
# input validation to ensure a three digit number is used

#input section
number = int(input("Please enter 3-d number you would like to calculate: "))

# input validation
if number < 100 or number > 999:
    print('Please use a three digit number.')
    exit()
# calculation
firstDigit = number//100
secondDigit = number%100//10
thirdDigit = number%10
sumOfDigits = firstDigit + secondDigit + thirdDigit

#output section
if sumOfDigits % 2 > 0:
    print("The sum of digits of number",number,"is an odd number.")
else:
    print("The sum of digits of number",number,"is an even number.")

# Written report
# Pretty simple to write, just need to check if the remainder after dividing by 2 is greater than zero,
# if it is than it is an odd number, if not even.