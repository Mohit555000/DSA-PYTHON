# https://leetcode.com/problems/running-sum-of-1d-array/description/

# class Solution:
#     def runningSum(self, nums: list[int]) -> list[int]:
#         prefix=[0]*(len(nums)+1)
#         for i in range(len(nums)):
#             prefix[i+1] = prefix[i] + nums[i]
#         return prefix[1:]
        

# time complexity is O(n)
# SPace complexity is O(n)