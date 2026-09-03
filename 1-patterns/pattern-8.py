# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# *********
#  *******
#   *****
#    ***
#     *


# Print the pattern in the function given to you.


# Example 1

class Solution:
    def pattern8(self, n):
        for i in range(n,0,-1):
            
            #spces
            for k in range(n-i):
                print(" ",end="")
            #stars
            for j in range(2*i-1):
                print("*",end="")
            print()
