# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# Print the pattern in the function given to you.
class Solution:
    def pattern20(self, n):
        #upper half
        for i in range(1,n+1):
            # upper left stars
            for j in range(1,i+1):
                print("*",end="")
            #upper middle spaces
            for k in range(2*(n-i)):
                print(" ",end="")
            #upper right stars
            for l in range(1,i+1):
                print("*",end="")
            print()
        for j in range(n-1,0,-1):
            #lower left stars
            for i in range(1,j+1):
                print("*",end="")
            #spaces
            for k in range(2*(n-j)):
                print(" ",end="")
            #lower right stars
            for m in range(1,j+1):
                print("*",end="")
            print()