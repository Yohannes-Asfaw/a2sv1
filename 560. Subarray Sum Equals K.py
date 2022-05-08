    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict=defaultdict(int)
        res=0
        s=0 
        for val in nums:
            s+=val
            if s==k:
                res+=1
            if s-k in mydict:
                res+=mydict[s-k]
            mydict[s]+=1
        return res
