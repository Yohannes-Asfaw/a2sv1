class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        small=[]
        for i in num:
            while len(small)>0 and small[-1]>i and k:
                small.pop()
                k-=1
            small.append(i)
        print(small)
        if k: 
            small = small[0:-k]
        if ''.join(small).lstrip('0')=="":
            return "0"
        else:
            return ''.join(small).lstrip('0')
