from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        freq=defaultdict(int)
        for ch in s:
            freq[ch]+=1
        for ch in t:
            freq[ch]-=1
            if freq[ch]<0:
                return False
        return True
        