# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# ABCDE

# ABCD

# ABC

# AB

# A

class Solution:
    def pattern15(self, n):
        for i in range(n,0,-1):
            for j in range(1,i+1):
                letter=chr(64+j)
                print(letter,end="")
            print()