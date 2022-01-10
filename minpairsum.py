    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nums1=[]
        i=0
        j=len(nums)-1
        while i<j:
            nums1.append(nums[i]+nums[j])
            i+=1
            j-=1



        return max(nums1)
