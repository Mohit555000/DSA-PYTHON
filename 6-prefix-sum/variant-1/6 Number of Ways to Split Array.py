#https://leetcode.com/problems/number-of-ways-to-split-array/description/

# approach 1
class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        count = 0
        for i in range(len(nums)-1):
            left+=nums[i]
            right = total - left
            if left >= right:
                count+=1
        return count
# Time complexity = O(n)
# SPace complexity = O(1)


#appraoch 2
class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        left = [0] * len(nums)
        right = [0] * len(nums)
        count = 0
        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range(1,len(nums)):
            left[i] = left[i-1] + nums[i]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] + nums[i]
        for i in range(len(nums)):
            if left[i]>=right[i]:
                count+=1
        return count

# time complexity  = O(n)
# space complexity = O(1)


