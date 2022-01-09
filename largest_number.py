   def largestNumber(self, nums: List[int]) -> str:
        if max(nums)==0:
            return "0"
        result = ""
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
        return result.join(list(map(str, nums)))
