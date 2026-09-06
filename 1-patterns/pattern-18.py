# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# E 

# D E 

# C D E 

# B C D E 

# A B C D E



# Print the pattern in the function given to you.

class Solution:
    def pattern18(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                letter=chr(64+(n-i+j))
                print(letter,end=" ")
            print()