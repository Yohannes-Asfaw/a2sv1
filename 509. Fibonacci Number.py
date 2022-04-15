class Solution:
    def fib(self, n: int) -> int:
        fib = []
        if n<=1:
            return n
        fib.append(0)
        fib.append(1)
        for i in range(2,n+1):
            fib.append(fib[i-1] + fib[i-2])

        return fib[-1]
