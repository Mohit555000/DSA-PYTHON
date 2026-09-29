# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left!=right:
            local_area=min(height[left],height[right])*(right-left)
            if local_area>max_area:
                max_area=local_area
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
        return max_area