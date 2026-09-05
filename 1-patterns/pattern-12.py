# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

class Solution:
    def pattern12(self, n):
        for i in range(1,n+1):
            #numbers
            for j in range(1,i+1):
                print(j,end="")
            #spaces
            for k in range(2*(n-i)):
                print(" ",end="")
            #numbers in reverse order
            for l in range(i,0,-1):
                print(l,end="")
            print()
