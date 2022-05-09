    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        num_odd, odd_idx, res =  0, [-1], 0
        for i in range(len(nums)):
            if nums[i] % 2:
                num_odd += 1
                odd_idx.append(i)
            
            if num_odd >= k:
                res +=  odd_idx[num_odd-k+1] - odd_idx[num_odd-k]
        
        return res
