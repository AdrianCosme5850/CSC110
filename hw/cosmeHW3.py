# Adrian Cosme-Halverson
# 11 JUL 23
# A program that takes in the coefficients of a quadratic equation and calculates how many 
# solutions the quadratic has.

# Imports

import math

# Welcome message

print('Hello! This program uses the coefficients of your quadratic equation to find the number of solutions.')
print('Please ensure that your quadratic is in standard form.')
# Inputs 

firstCoefficient = int(input('Please input the coefficients of your quadratic equation. '))
secondCoefficient = int(input('Please input the second coefficient of your quadratic equation. '))
thirdCoefficient = int(input('Please input the third coefficient of your quadratic equation. '))

# Calculations and Outputs

if(firstCoefficient != 0 and secondCoefficient != 0 or thirdCoefficient != 0):
    discriminant = secondCoefficient**2 - 4 * firstCoefficient * thirdCoefficient
    if(discriminant > 0):
        firstSolution = (-secondCoefficient + math.sqrt(discriminant))/(2*firstCoefficient)
        secondSolution = (-secondCoefficient - math.sqrt(discriminant))/(2*firstCoefficient)
        print('The equation ' + format(firstCoefficient, '.2f') +'^2 + ' + format(secondCoefficient, '.2f') +'x + ' + format(thirdCoefficient, '.2f') + ' = 0 has two solutions.')
        print('x = ' + format(firstSolution, '.2f') + ' or x = ' + format(secondSolution, '.2f') + '.')
    elif(discriminant == 0):
                solution = -secondCoefficient/(2*firstCoefficient)
                print('The equation ' + format(firstCoefficient, '.2f') +'^2 + ' + format(secondCoefficient, '.2f') +'x + ' + format(thirdCoefficient, '.2f') + ' = 0 has one solution.')
                print('x = ' + format(solution, '.2f') + '.')
    else:
        print('The equation has no solutions.')
else: 
    print('Please use standard form!')    

# Written Report
# I spent more time trying to figure out why my inputs and outputs were wront than I did writing the program.
# I added the error message at the end this time.