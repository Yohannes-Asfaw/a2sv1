 def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:   
        newlist = []
        for i in nums:
            m = 0
            for j in nums:
                if j < i:
                    m += 1
            newlist.append(m)
        return newlist
