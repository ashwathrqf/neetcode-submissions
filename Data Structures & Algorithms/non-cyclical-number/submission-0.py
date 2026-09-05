class Solution:
    def isHappy(self, n: int) -> bool:
        def op(a):
            return sum(int(i)**2 for i in str(a))
        seen=set()
        while n not in seen:
            if n==1:
                return True
            seen.add(n)
            n=op(n)
        return False
        
        