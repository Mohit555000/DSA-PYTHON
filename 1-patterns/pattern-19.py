# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


# Print the pattern in the function given to you.


class Solution:
    def pattern19(self, n):
        for j in range(n,0,-1):
            for m in range(1,j+1):
                print("*",end="")
            #upper part having space
            for z in range(2*(n-j)):
                print(" ",end="")
            #upper right part
            for a in range(1,j+1):
                print("*",end="")
            print()
        for i in range(1,n+1):
            #lower left part
            for j in range(1,i+1):
                print("*",end="")
            # lower part having space
            for k in range(2*(n-i)):
                print(" ",end="")
            #lower right part
            for l in range(1,i+1):
                print("*",end="")
            print()
            
            
