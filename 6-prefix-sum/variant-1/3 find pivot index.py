# https://leetcode.com/problems/find-pivot-index/description/


# Appraoch 1
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        left=[0]*(len(nums))
        for i in range(1,len(nums)):
            left[i] = left[i-1] + nums[i-1]
        right = [0]*(len(nums)+1)
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] + nums[i+1]

        for i in range(len(nums)):
            if left[i]==right[i]:
                return i
        return -1 

# Appraocb 2
total = sum(nums)
left = 0
for i in range(len(nums)):
    if left == total - left - nums[i]:
        return i
    left += nums[i]
return -1


# time complexity is O(n)
# SPace complexity is O(n)