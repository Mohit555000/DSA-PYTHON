# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

# Method 1 convert the number into string and return the reverse of the string.
class Solution:
    def reverseNumber(self, n):
        sign= -1 if n<0 else 1
        return sign*int(str(abs(n))[::-1])

#MEthod 2 Maths
class Solution:
    def reverseNumber(self, n):
        sign=-1 if n<0 else 1
        n=abs(n)
        reversed_digit=0
        while n>0:
            last_digit=n%10
            reversed_digit=reversed_digit*10+last_digit
            n=n//10
        return reversed_digit