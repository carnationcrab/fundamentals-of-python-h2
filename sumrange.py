# SAM MARTORANA

# ################################ [H2_3] ################################# #
# Write a program that reads integers start and stop from the user, then
# calculates and prints the sum of the squares of each integer ranging from
# start to stop, inclusive. "Inclusive" means that both the values start and
# stop are included.
#
# For example, if you enter 2 and 4, your program should print 29 since
# 2**2 + 3**2 + 4**2 == 4+9+16 == 29. Hint: use an accumulator variable.
# Initialize it before the loop to 0, then add the square of the current loop
# variable to it within the loop body.
# ########################################################################## #


start = int(input('start: '))
stop = int(input('stop: '))

total = 0

for integer in range(start, stop + 1, 1):
    total = total + integer ** 2


print(total)