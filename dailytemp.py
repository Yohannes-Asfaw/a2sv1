    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range(1,len(temperatures)):
            if temperatures[i]>temperatures[i-1]:
                ans[i-1]=1
                while stack:
                    if temperatures[stack[-1]]<temperatures[i]:
                        ans[stack[-1]]=i-stack[-1]
                        stack.pop()
                    else:
                        break    
            else:
                stack.append(i-1)
        return ans
