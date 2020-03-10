# SAM MARTORANA

# ################################ [H2_2] ################################# #
# Write a program that uses loops of the form:  
#
# for num in range(…):
#     print (num,end=' ') # end='' keeps loop output on same line  
#     print () # start new line  
#
# to print out each of the sequences below.  
# You MUST use a for loop like the above, with range(x,y,z) for some int
# values of x, y, z for each.
#  
# 1 2 3 4 5 6 7 8 9 10
# 1 3 5 7 9 11 13
# 47 23
# 10 9 8 7 6 5 4 3 2 1
# 20 16 12 8 4 0
# 3 9 15 21 27 33 
# ########################################################################## #

def printer(x, y, z):
    for num in range(x, y, z):
        print(num, end=' ')
    print()


printer(1, 11, 1)
printer(1, 14, 2)
printer(47, 20, -24)
printer(10, 0, -1)
printer(20, -1, -4)
printer(3, 34, 6)
