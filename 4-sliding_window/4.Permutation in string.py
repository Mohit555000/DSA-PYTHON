class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m=len(s1),len(s2)
        if n>m:
            return False
        s1_count=[0]*26
        window_count=[0]*26
        for c in s1:
            s1_count[ord(c)-ord('a')]+=1
        left=0
        for right in range(m):
            window_count[ord(s2[right])-ord('a')]+=1

            if right>=n:
                window_count[ord(s2[left])-ord('a')]-=1
                left+=1
            if window_count==s1_count:
                return True
        return False


        