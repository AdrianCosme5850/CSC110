# Adrian Cosme-Halverson
# 5 JUL 23
# A program that works as a tip calculator for a restaurant. 
# It takes in an amount to be paid and a desired tip percentage.
# It then gives out a formatted bill including tip.

# Start of Inputs
subTotal = float(input('How much is the bill? '))
tipPer = float(input('What percent tip do you want to give? '))
tipPercent = tipPer/100 #turned the user inputted tax into a proper percentage.

# calculations

salesTax = 0.095
total = format(subTotal+subTotal*salesTax, '.2f') #Used the format function to round to two decimals for me.
tip = format(subTotal*tipPercent, '.2f') 
totalAndTip = format(subTotal+subTotal*salesTax + subTotal*tipPercent, '.2f')

# Outputs 

print(format('Amount of bill: ')+ format(subTotal, '.2f'))
print(format("Tip percent: ") + format(tipPer, '.0f'))
print("*"*30)
print(format("Subtotal", '20s') + '$' +format(subTotal, '.2f'))
print(format('Sales Tax', '20s') + '$' + format(subTotal * salesTax, '.2f'))
print('-'*30)
print(format('Total', '20s') + '$' + total)
print(format('Tips', '20s') + '$' + tip)
print('*'*30)
print(format('Balance Due', '20s') + '$' + totalAndTip)
print('Thank you!')


# Report
# Had some trouble figuring out how to use the formatting function. There
# are a few areas that could be cut down and simplified. Will probably
# spend more time planning the program before hoping into coding.

# Resubmit
# Redid the print statements to use '*'*30 instead of individual whitespaces, and used format for all of the numbers
# Works a lot better now.