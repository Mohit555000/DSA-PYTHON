# You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.



# A palindrome number is a number which reads the same both left to right and right to left.


# Example 1

# Input: n = 121

# Output: true

# Explanation: When read from left to right : 121.

# When read from right to left : 121.

# Example 2

# Input: n = 123

# Output: false

# Explanation: When read from left to right : 123.

# When read from right to left : 321.

# Example 3

# Input: 101

# Output:

# true

#Method 1 convert the number into string and check if the string is equal to its reverse.

class Solution:
    def isPalindrome(self, n):
        if n<0:
            return False
        s=str(n)
        if s==s[::-1]:
            return True
        else:
            return False

#Method 2 Maths
class Solution:
    def isPalindrome(self, n):
        if n<0:
            return False
        n=abs(n)
        reversed_number=0;
        original=n
        while n>0:
            last_digit=n%10
            reversed_number=reversed_number*10+last_digit
            n=n//10
        if reversed_number==original:
            return True
        else:
            return False