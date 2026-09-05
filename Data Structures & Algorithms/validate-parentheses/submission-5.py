class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ref={
            '(':')',
            '{':'}',
            '[':']',
        }
        for ch in s:
            if ch in ref:
                stack.append(ch)
            elif stack and ref[stack[-1]]==ch:
                stack.pop()
            else:
                return False
        return not stack

        