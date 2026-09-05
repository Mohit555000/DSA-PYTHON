# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# 1 

# 2 3 

# 4 5 6 

# 7 8 9 10 

# 11 12 13 14 15



# Print the pattern in the function given to you.


# Example 1


class Solution:
    def pattern13(self, n):
        #your code goes here
        count=1
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(count,end=" ")
                count=count+1
            print()