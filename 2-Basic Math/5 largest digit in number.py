# Return the Largest Digit in a Number
# Easy

# Company
# You are given an integer n. Return the largest digit present in the number.


# Example 1

# Input: n = 25

# Output: 5

# Explanation: The largest digit in 25 is 5.

# Example 2

# Input: n = 99

# Output: 9

# Explanation: The largest digit in 99 is 9.

# Example 3

# Input: n = 1

# Output:

# 1

class Solution:
    def largestDigit(self, n):
        largestDigit=0
        n=abs(n)
        while n>0:
            last_digit=n%10
            n=n//10
            if largestDigit<last_digit:
                largestDigit=last_digit
        return largestDigit
