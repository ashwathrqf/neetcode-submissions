class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops=['+','-','*','/']
        for t in tokens:
            if t in ops:
                b=stack.pop()
                a=stack.pop()
                if t=="+":
                    res=a+b
                elif t=="-":
                    res=a-b
                elif t=="*":
                    res=a*b
                else:
                    res=int(a/b)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]
            
                    

            


        