class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number_of_zeros=nums.count(0)
        for i in range(len(nums)):
            if number_of_zeros==0:
                break
            if nums[i]==0:
                number_of_zeros-=1
                nums.append(nums[i])
                nums.remove(nums[i])
        
