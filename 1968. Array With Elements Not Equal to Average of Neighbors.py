class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        check=1
        while check:
            check=0
            i = len(nums)-2
            while i >= 0:
                if (nums[i+1] + nums[i-1]) / 2 == nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    check=1
                i -= 1
                
        return nums
          
