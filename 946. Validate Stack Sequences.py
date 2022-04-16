class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        check=[]
        i=0
        for j in pushed:
            check.append(j)
            while len(check)>0 and check[-1]==popped[i]:
                check.pop()
                i+=1
        return len(check)==0
