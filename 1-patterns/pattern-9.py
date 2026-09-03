# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



#     * 
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *


# Print the pattern in the function given to you.


# Example 1

# Input: n = 4

# Output:



# Example 2

# Input: n = 2

# Output:

class Solution:
    def pattern9(self, n):
        for i in range(n):
            #space
            for j in range(n-i-1):
                print(" ",end="")
            #star
            for k in range(2*i+1):
                print("*",end="")
            print()
        for a in range(n,0,-1):
            #space
            for i in range(n-a):
                print(" ",end="")
            #star
            for j in range(2*a-1):
                print("*",end="")
            print()