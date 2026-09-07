# You are given an integer n. You need to return the number of digits in the number.



# The number will have no leading zeroes, except when the number is 0 itself.

# Method 1 convert the number into string and return the length of the string.
class Solution:
    def countDigit(self, n):
        return len(str(abs(n)))

# Method 2 
class Solution:
    def countDigit(self, n):
        n=abs(n)
        count=0
        if n==0:
            return 1
        while n>0:
            n=n//10
            count=count+1
        return count

# "/" this is normal division operator which returns float value. for example 5/2=2.5
# "//" this is floor division operator which returns nearest integer value. for example 5//2=2
        