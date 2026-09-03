# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# *

# **

# ***

# ****

# *****

# ****

# ***

# **

# *



# Print the pattern in the function given to you.


# Example 1

# Input: n = 4

# Output:



# Example 2

# Input: n = 2

# Output:



# Constraints

# 1 <= n <= 100


class Solution:
    def pattern10(self, n):
        #UPPER PART
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            print()
        #LOWER PART
        for j in range(n-1,0,-1):
            for i in range(j):
                print("*",end="")
            print()
            


