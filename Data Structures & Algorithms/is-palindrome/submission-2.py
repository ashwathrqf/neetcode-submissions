class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lst_str=[]
        # for ch in s:
        #     if ch.isalnum():
        #         lst_str.append(ch.lower())
        # for i in range(len(lst_str)//2):
        #     left=lst_str[i]
        #     right=lst_str[len(lst_str)-1-i]
        #     if left!=right:
        #         return False
        # return True
        left=0
        right=len(s)-1
        while left<right:
            while not s[left].isalnum() and left<right:
                left+=1
            while not s[right].isalnum() and left<right:
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
            


        