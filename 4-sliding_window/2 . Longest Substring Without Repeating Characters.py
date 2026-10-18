#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        left=0
        right=0
        max_count=0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            max_count=max(max_count,right-left+1)
        return max_count
        
        