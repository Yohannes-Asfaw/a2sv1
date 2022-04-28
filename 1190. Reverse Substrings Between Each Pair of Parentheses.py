class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        tempo=[]
        for i in s:
            if i!=')':
                stack.append(i)
            elif i==')':
                tempo.clear()
                while stack[-1]!='(':
                    tempo.append(stack.pop())
                stack.pop()
                for i in tempo:
                    stack.append(i)
                    
        return "".join(stack)
    
