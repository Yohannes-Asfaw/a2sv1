    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        counter = 0
        an = 0
        while j < len(nums):
            if nums[j] == 0 and counter == k:
                while nums[i] != 0:
                    i += 1
                i += 1
                counter -= 1
            if nums[j] == 0:
                counter += 1
            j += 1
            an = max(an, j-i)
        return an
                
