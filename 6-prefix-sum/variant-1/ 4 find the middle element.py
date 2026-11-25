# https://leetcode.com/problems/find-the-middle-index-in-array/description/

class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        left=0
        for i in range(len(nums)):
            if left == total - left - nums[i]:
                return i
            left+=nums[i]
        return -1
    
# same as question 3
# time complexity = O(n)
# SPace complexity = O(1)

