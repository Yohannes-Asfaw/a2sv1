class Solution:
    def decodeString(self, s: str) -> str:
        set1 = ''
        j = 0
        for i in s:
            if i == '[' or i == ']':
                set1 += ' ' + i + ' '
            elif i.isnumeric() and not s[j - 1].isnumeric():
                set1 += ' ' + i

            else:
                set1 += i

            j += 1
        set2 = set1.split()
        stack = []

        j = 0
        for i in set2:

            if i.isnumeric():
                stack.append(i)

            elif i.isalpha():
                stack.append(i)
                if len(stack)>1 and stack[-1].isalpha() and stack[-2].isalpha():
                    ans = (stack[-2]) + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(ans)

            elif i == ']':
                if stack[-2].isnumeric():
                    ans = int(stack[-2]) * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(ans)
                elif  stack[-3].isnumeric():
                    ans = int(stack[-3]) * ((stack[-2]) + stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append(ans)

            j += 1

        return (''.join(stack))
