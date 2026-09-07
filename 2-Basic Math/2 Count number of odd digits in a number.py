# You are given an integer n. You need to return the number of odd digits present in the number.



# The number will have no leading zeroes, except when the number is 0 itself.


# Example 1

# Input: n = 5

# Output: 1

# Explanation: 5 is an odd digit.

# Example 2

# Input: n = 25

# Output: 1

# Explanation: The only odd digit in 25 is 5.

# Example 3

# Input: n = 15

# Output:

# 2
class Solution:
    def countOddDigit(self, n):
        n=abs(n)
        if n==0:
            return 0
        count=0
        while n>0:
            last_digit=n%10
            n=n//10
            if last_digit%2!=0:
                count=count+1
        return count