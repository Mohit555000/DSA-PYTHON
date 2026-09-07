# You are given an integer n. You need to find out the number of prime numbers in the range [1, n] (inclusive). Return the number of prime numbers in the range.



# A prime number is a number which has no divisors except, 1 and itself.


# Example 1

# Input: n = 6

# Output: 3

# Explanation: Prime numbers in the range [1, 6] are 2, 3, 5.

# Example 2

# Input: n = 10

# Output: 4

# Explanation: Prime numbers in the range [1, 10] are 2, 3, 5, 7.

# Example 3

# Input: n = 20

# Output:

# 8
# Constraints

class Solution:
    def primeUptoN(self, n):
        count = 0
        for i in range(2, n + 1):          # check every number from 2 to n inclusive
            is_prime = True                 # assume i is prime until proven otherwise
            for j in range(2, i):
                if i % j == 0:               # found a divisor — i is NOT prime
                    is_prime = False
                    break                     # no need to check further
            if is_prime:
                count = count + 1
        return count