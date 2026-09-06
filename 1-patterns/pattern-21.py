# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# *****
# *   *
# *   *
# *   *
# *****


# Print the pattern in the function given to you.


# Example 1

# Input: n = 4

# Output:



# Example 2

# Input: n = 2

# Output:

class Solution:
    def pattern21(self, n):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==1 or i==n:
                    print("*",end="")
                elif j==1 or j==n:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()