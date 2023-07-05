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

print('Amount of bill: $' + str(subTotal))
print("Tip percent: " + str(int(tipPer)))
print("***************")
print("Subtotal             $" + str(subTotal))
print("Sales Tax             $" + format(subTotal * salesTax, '.2f'))
print('     --------       ')
print('Total                   $' + total)
print('Tips                    $' + tip)
print('**********************')
print('Balance due              $' + totalAndTip)
print('Thank you!')


# Report
# Had some trouble figuring out how to use the formatting function. There
# are a few areas that could be cut down and simplified. Will probably
# spend more time planning the program before hoping into coding.