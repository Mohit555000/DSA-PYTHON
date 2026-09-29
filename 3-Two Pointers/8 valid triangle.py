# https://leetcode.com/problems/valid-triangle-number/


#Brute FOrce
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        count=0
        ans=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if (nums[i]>0 and nums[j]>0 and nums[k]>0):
                        if (nums[i]+nums[j]> nums[k] and nums[j]+nums[k]>nums[i] and nums[i]+nums[k]>nums[j]):
                            count+=1
        return count


# Optimized Approach
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count=0
        for k in range(len(nums)-1,1,-1):
            i=0
            j=k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    count=count+(j-i)
                    j=j-1
                else:
                    i=i+1
        return count
                
        