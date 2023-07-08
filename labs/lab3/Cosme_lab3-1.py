# Adrian Cosme-Halverson
# 08 JUL 23
# A tip calculator, in this version input validation is added to ensure the user puts in information
# that can be used.

# create a constant
TAX = 9.5

# input section
bill = float(input("The amount of the bill: "))
tips = float(input("The percentage tip: "))

# input validation
if tips >= 100:
    print('Your tip should not exceed 100%!')
    exit()
# processing
totalTips = bill * tips/100
totalTax = bill * TAX/100
totalBill = totalTips + totalTax
subTotal = bill + totalTax
total = subTotal + totalTips

# output
print("Here is your restaurant bill")
print("*" * 30)
print(format("Subtotal", '20s'), "$" + format(bill, '.2f'))
print(format("Sales tax", '20s'), "$" + format(totalTax, '.2f'))
print(format(' ', '20s') + '-'*10)
print(format("Total", '20s'), "$" + format(subTotal, '.2f'))
print(format("Tips", '20s'), "$" + format(totalTips, '.2f'))
print("*" * 30)
print(format("Balance due", '20s'), "$" + format(total, '.2f'))
print()
print(format("Thank you!", '10s'), ' ')


# Written report
# Added a simple if statement to check to make sure the tip percentage does not exceed 100%.
# I used the exit function just to experiment, will use else statement in future part of lab.