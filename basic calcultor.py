import math
class Solution:
    def calculate(self, s: str) -> int:
      
        s= s.replace(' ', '')
        stack = []

        j = 0
        oprator = ['+', '-', '*', '/']
        set1=''
        for i in s:
            if i.isnumeric():
                set1+=i

            elif not i.isnumeric():
                set1+=' '+i+' '
        str=set1.split()

        for i in str:
            if j == 0:
                stack.append(int(str[0]))
            elif i == '+':
                stack.append(int(str[j + 1]))
                if len(stack) > 1 and  j+2 < len(str) and str[j + 2] !='*'  and str[j + 2] !='/' :
                    ans = stack[-1] + stack[-2]
                    stack.pop()
                    stack[-1]=ans
            elif i == '-':
                stack.append(-int(str[j + 1]))
                if len(stack) > 1 and  j+2 < len(str) and str[j + 2] !='*'  and str[j + 2] !='/':
                    ans = stack[-1] + stack[-2]
                    stack.pop()
                    stack[-1]=ans
            elif i == '*':
                ans = stack[-1] * int(str[j + 1])
                stack.pop()
                stack.append(ans)
                if len(stack) > 1  and  j+2 < len(str) and str[j + 2] !='*'  and str[j + 2] !='/':
                    ans2 = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(ans2)
            elif i == '/':
                if stack[-1]<0:
                    ans = math.ceil(stack[-1] / int(str[j + 1]))
                    stack.pop()
                    stack.append(ans)
                elif  stack[-1]>0:
                    ans = math.floor(stack[-1] / int(str[j + 1]))
                    stack.pop()
                    stack.append(ans)
                if len(stack) > 1  and  j+2 < len(str) and str[j + 2] !='*'  and str[j + 2] !='/':
                    ans2 = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(ans2)
          
            j += 1
        if len(stack) > 1:
            result = stack[-1] + stack[-2]
            return (result)
        else:
            return (stack[0])
