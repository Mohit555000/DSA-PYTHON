# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA


# Print the pattern in the function given to you.


# Example 1

# Input: n = 4

# Output:



# Example 2

# Input: n = 2

# Output:

class Solution:
    def pattern17(self, n):
        for i in range(1,n+1):
            #space
            for j in range(n-i):
                print(" ",end="")
            #letters
            for k in range(1,i+1):
                letter=chr(64+k)
                print(letter,end="")
            #falling letters
            for l in range(i-1,0,-1):
                letter=chr(64+l)
                print(letter,end="")
            print()
            