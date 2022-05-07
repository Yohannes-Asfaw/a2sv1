    def findTheWinner(self, n: int, k: int) -> int:
        stack=[]
        for i in range(n+1):
            stack.append(i)
        i=-1
        stack.pop(0)
        while(len(stack)>1):
            i+=k
            i=i%len(stack)
            stack.pop(i)
            i-=1
        return stack[0]
            
            
