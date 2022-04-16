class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n!=0:
            m=x//n
        a=x
        def power(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            else:
                n -= m
                x = x * a
        return pow(x, n)
