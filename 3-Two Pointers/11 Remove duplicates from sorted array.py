# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left=1
        right=1
        n=len(nums)
        while right<n:
            if nums[left-1]==nums[right]:
                right+=1
            else:
                nums[left]=nums[right]
                left+=1
                right+=1
        return left


        