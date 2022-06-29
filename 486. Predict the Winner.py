class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            if right < left:
                return 0 
            if right == left: 
                return nums[left] 
            if (left, right) in memo:
                return memo[(left, right)] 
            left_right = helper(left + 1, right - 1)
            print(left_right)
            left_left = helper(left + 2, right) 
            print(left_left)
            take_left = nums[left] + min(left_right - nums[right], left_left - nums[left + 1])
            print(take_left)
            
            right_right = helper(left, right - 2)
            print( right_right)
            take_right = nums[right] + min(left_right - nums[left], right_right - nums[right - 1]) 
            print(take_right)
            result = max(take_left, take_right) 
            memo[(left, right)] = result 
            print(result)
            return result 
        
        memo = {} 
        return helper(0, len(nums) - 1) >= 0
