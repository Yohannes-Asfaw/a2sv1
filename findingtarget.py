 def targetIndices(self, nums: List[int], target: int) -> List[int]:
        z = []
        nums.sort()
        j = 0
        for i in nums:
            if i == target:
                z.append(j)
            j += 1

        return z
