    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num3=[]
        for i in nums1:
            check = True
            for j in nums2[nums2.index(i):]:
                if j > i:
                    num3.append(j)
                    check=False
                    break
            if check:
                num3.append(-1)
        return num3
