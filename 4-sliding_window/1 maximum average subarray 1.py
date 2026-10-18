#https://leetcode.com/problems/maximum-average-subarray-i/description/

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left=0
        right=k-1

        #building first window
        window_sum=sum(nums[left:right+1])
        max_sum=window_sum

        while right<len(nums)-1:
            left+=1
            right+=1
            window_sum=window_sum+nums[right]-nums[left-1]
            max_sum=max(window_sum,max_sum)
        return max_sum/k
        

