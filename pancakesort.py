    def pancakeSort(self, nums: List[int]) -> List[int]:
        nums1=nums.copy()
        nums1.sort()
        result=[]
        n=0
        length=len(nums)
        for i in nums1:
            k = nums.index(nums1[-1-n])+1
            result.append(k)
            nums[:k] = nums[:k][::-1]
            nums[:length] = nums[:length][::-1]
            result.append(length)
            n+=1
            length-=1
            if nums==nums1:
                return result
