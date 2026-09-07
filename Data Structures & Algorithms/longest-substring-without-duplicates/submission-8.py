class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count=0
        seen={}
        l=0
        for r in range(len(s)):
            if s[r] in seen:
                l=max(l,seen[s[r]]+1)
            seen[s[r]]=r
            max_count=max(max_count,r-l+1)
        return max_count


        