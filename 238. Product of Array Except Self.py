    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        pre_times, post_times = nums[0], nums[-1]         
            
        for i in range(1, n):
            result[i] = pre_times 
            pre_times *= nums[i]
        print(result)
        for i in range(n-2, -1, -1):
            result[i] *= post_times 
            post_times *= nums[i]
        
        return result
