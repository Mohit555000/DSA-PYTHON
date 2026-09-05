# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# 1 

# 0 1 

# 1 0 1 

# 0 1 0 1 

# 1 0 1 0 1



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
    def pattern11(self, n):
        for i in range(1,n+1):
            num = 0 if i%2==0 else 1
            for j in range(i):
                print(num,end=" ")
                num=1-num
            print()
             