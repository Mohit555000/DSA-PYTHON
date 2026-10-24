#https://leetcode.com/problems/fruit-into-baskets/
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        frequency = {}
        left = 0
        baskets = 2
        max_length = 0
        for right in range(len(fruits)):
            frequency[fruits[right]] = frequency.get(fruits[right], 0) + 1
            while len(frequency) > baskets:
                frequency[fruits[left]] -= 1
                if frequency[fruits[left]] == 0:
                    del frequency[fruits[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length