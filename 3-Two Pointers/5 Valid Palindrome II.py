# https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        flag=True
        left=0
        right=len(s)-1
        while(left<=right):
            local_flag=True
            if s[left]!=s[right]:
                local_flag=False
            flag=flag or local_flag
            left=left+1
            right=right-1
        return flag
        