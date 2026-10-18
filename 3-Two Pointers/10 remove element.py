# https://leetcode.com/problems/remove-element/description/
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n=len(nums)
        left=0
        right=len(nums)-1
        count=0
        while left<n and left<right:
            if nums[left]!=val:
                left+=1
            elif nums[left]==val and nums[right]==val:
                right-=1
            else:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        for i in range(n):
            if nums[i]==val:
                count+=1
        return n-count