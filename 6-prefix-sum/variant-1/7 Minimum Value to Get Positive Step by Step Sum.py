#https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
#Appraoch A brute force appraoch
class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        start = 1
        while True:
            total = start
            valid = True
            for x in nums:
                total = total + x
                if total <1:
                    valid = False
                    break
            if valid:
                return start
            start +=1

# time complexity = O(n*answers)
# space complexity is O(1)

#approach B
class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        start = 1
        total = 1
        for x in nums:
            total+=x
            if total <1:
                start = start + (1-total)
                total = 1
        return start

# Time complexity = O(n)
# Space Complexity = O(1)
