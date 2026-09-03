from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        freq_s=defaultdict(int)
        freq_t=defaultdict(int)
        for i in range(n):
            freq_s[s[i]]+=1
            freq_t[t[i]]+=1
        for al in freq_s.keys():
            if freq_s[al]!=freq_t[al]:
                return False
        return True
        