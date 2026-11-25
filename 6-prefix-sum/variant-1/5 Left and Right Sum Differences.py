#https://leetcode.com/problems/left-and-right-sum-differences/

# Appraoch A
n = len(nums)
left = [0] * n
right = [0] * n
result = [0] * n

for i in range(1, n):                    # start at 1, left[0] = 0
    left[i] = left[i - 1] + nums[i - 1]

for i in range(n - 2, -1, -1):           # start at n-2, right[n-1] = 0
    right[i] = right[i + 1] + nums[i + 1]

for i in range(n):
    result[i] = abs(left[i] - right[i])
return result

#approach B
# O(1) extra space version

total = sum(nums)
left = 0
result = []
for x in nums:
    right = total - left - x
    result.append(abs(left - right))
    left += x                            # add AFTER computing right
return result