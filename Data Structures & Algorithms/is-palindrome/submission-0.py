class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst_str=[]
        for ch in s:
            if ch.isalnum():
                lst_str.append(ch.lower())
        for i in range(len(lst_str)//2):
            left=lst_str[i]
            right=lst_str[len(lst_str)-1-i]
            if left!=right:
                return False
        return True


        