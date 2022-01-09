    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums) - 1):
            if len(nums) > 3:
                if nums[i] == (nums[i - 1] + nums[i + 1]) / 2 and i + 2 < len(nums):
                    nums[0], nums[i+1] = nums[i+1], nums[0]
                    nums[i+1], nums[-1] = nums[-1], nums[i+1]
                elif nums[i] == (nums[i - 1] + nums[i + 1]) / 2 and i + 2 == len(nums):
                    nums[0], nums[i+1] = nums[i+1], nums[0]
                    nums[i+1],nums[-1]=nums[-1],nums[i+1]

        else:
            if nums[i] == (nums[i - 1] + nums[i + 1]) / 2:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        if len(nums) % 2!=0:
            for i in range(1, len(nums) - 1):
                if len(nums) > 3:
                    if nums[i] == (nums[i - 1] + nums[i + 1]) / 2 and i + 2 <= len(nums):
                            nums[0], nums[i] = nums[i], nums[0]

        return nums
