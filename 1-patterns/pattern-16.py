# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# A

# BB

# CCC

# DDDD

# EEEEE

class Solution:
    def pattern16(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                letter=chr(64+i)
                print(letter,end="")
            print()