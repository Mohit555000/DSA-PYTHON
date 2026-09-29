# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans=[0]*len(nums)
        left=0
        right=len(nums)-1
        position=len(nums)-1
        while(left<=right and position>=0):
            if nums[right]*nums[right]>nums[left]*nums[left]:
                ans[position]=nums[right]*nums[right]
                right=right-1
            else:
                ans[position]=nums[left]*nums[left]
                left=left+1
            position=position-1
        return ans
        