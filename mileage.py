# SAM MARTORANA

# ################################ [H2_4] ################################# #
# Do Exercise 10 at the end of HTT2 (in HTT2.13). Read each value as float
# (read as string st then convert using typecast function float(st)). 
#
# Write a program that will compute MPG for a car. Prompt the user to enter
# the number of miles driven and the number of gallons used. Print a nice
# message with the answer.
# ########################################################################## #

def calcMPG(miles, gals):
    mpg = miles / gals
    return (mpg)


ms = float(input('miles: '))
gs = float(input('gallons: '))

print('The MPG of your vehicle is', calcMPG(
    ms, gs
), 'miles per gallon')