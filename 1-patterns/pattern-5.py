# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# *****

# ****

# ***

# **

# *

class Solution:
    def pattern5(self, n):
        for i in range(n,0,-1):
            for j in range(i):
                print("*",end="")
            print()

here we have to print the pattern in decreasing order so the outer loop will start from n and it will go upto 1 and to dcras i by 1 in python we have to mention -1 to make it less. th default behaviour of range function is that it just increses
