    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)   
        ans= not stack   
        
        return ans
