class Solution:
    def isValid(self, s: str) -> bool:
        cout = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        list1 = []
        for i in s:
            if i in cout.keys():
                list1.append(i)
                continue
            if len(list1)==0:
                return False
            elif i in cout.values():
                if cout[list1[-1]] == i:
                  list1.pop()
                else:
                    return False
        if len(list1) == 0:
            return True
        else:
            return False
