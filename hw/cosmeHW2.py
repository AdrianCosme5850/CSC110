# Adrian Cosme-Halverson
# 06 JUL 23
# A program that determines the cost for siding of a rectangular house. Requires the dimensions of the house, along with the price
# of profiles, nails, and siding strips.

# imports
import math

# Welcome message

print('Hello! This program determines the cost of siding for your house.')
print('In order to determine the cost please have the length, width, and height of your home')
print('along with the price for profiles, siding nails, and side strips prepared.')

# inputs

length = int(input('Please enter the length of the house in feet: '))
width = int(input('Please input the width of your house in feet: '))
height = int(input('Please input the height of your house in feet: '))
profilePrice = float(input('Please input the cost of your profiles in $: '))
sidingNailPrice = float(input('Please input the cost of your siding nails per box in $'))
stripPrice = float(input('Please input the cost of your side strips in $:'))

# Start of the calculations 

houseLateralSurfaceArea = 2*(length + width) * height * 0.8

houseLateralSurfaceAreaInches = houseLateralSurfaceArea * 144 #Convert the surface area to inches to more easily find the necessary amount of profiles

profile = math.ceil(houseLateralSurfaceAreaInches / 288) #Surface area in inches is divided by the profile surface area and rounded up

sidingNail = math.ceil(profile / 2) 

strip = math.ceil(profile * (2/3))

# Determine the cost for all materials and add together
profileCost = profilePrice * profile
sidingNailCost = sidingNail * sidingNailPrice
stripCost = strip * stripPrice

totalCost = profileCost + sidingNailCost + stripCost

# Start of output

print('The house has a length = ' + str(length) + ', width = ' + str(width) + ', height = ' + str(height))
print('SIDING')
print('*'*20)
print(format('Total area of siding is', '40s') + format(houseLateralSurfaceArea, ',.2f') + ' feet squared') # Using the , specification to set a comma in the thousandths place
print(format('Total profile is', '40s') + format(profile, ',.0f'))
print(format('Boxes of siding nails are', '40s') + format(sidingNail, ',.0f'))
print(format('Weather side strips are', '40s') + format(strip, ',.0f'))
print('*'*20)
print('TOTAL')
print('*'*20)
print(format('The cost of materials for siding', '40s')+ '$' + format(totalCost, ',.2f'))

# Written report
# I started by whiteboarding out the requirements of the assignment on a miro board, then whiteboard out what each part of the program was going to look like.
# Coding the entire assignment took around 20 minutes, however I was stuck for a few hours trying to determine what the formula was to find the siding and profiles of a house.
# I don't know anything about putting siding on houses, and the assignment says "calculate the cost of materials for siding and roof", so I kept thinking I needed to include
# the dimensions of a roof somewhere. After a couple of hours of fiddling around trying different formulas I looked it up online and realised I needed to find the lateral surface
# area of a rectangular prism. After that I coded half the assignment but got held up again by the profiles. I didn't know what a profile was or how it factored into the siding of 
# a house, so I tried dividing the lateral surface area of the house in inches by 288(32*9). When that didn't work I spent around a half hour on the internet trying to figure out
# if profiles were used in roofing somehow (the assignment says that we need to "calculate the cost of materials for siding and roof"). After messing with that for awhile I finally 
# figured out I had converted square feet to square inches incorrectly. Otherwise I wanted to get commas into my numbers, so that they were more readable. This took around five
# minutes for me to find the correct format specification.
# I tested the program using 10s and 20s across the board. All of the results came back as I had calculated them. I learned a little bit about how the format 
# function works. As far as things I would do differently, next time I will just email you if something in an assignment confuses me. I couldn't this time as I have
# been working full-time and going to school full-time, so this is the only time I could find to do the assignment and it is due tonight. However, if I can help it 
# I will try to get some of it in beforehand to email you with any issues.