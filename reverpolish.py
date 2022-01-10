    def evalRPN(self, tokens: List[str]) -> int:
        oprator=['+','/','-','*']
        stack=[]
        ans=0
        for i in tokens:
            if i not in oprator:
                stack.append(int(i))
            else:
                if i=='+':
                    ans=int(stack[-1])+int(stack[-2])
                elif i == '-':
                    ans = int(stack[-2]) - int(stack[-1])
                elif i == '*':
                    ans = int(stack[-1]) * int(stack[-2])
                elif i=='/':
                    ans = int(stack[-2]) / int(stack[-1])
                    if ans < 0:
                        ans=ceil(ans)
                    else:
                        ans=floor(ans)
                stack.pop()
                stack.pop()
