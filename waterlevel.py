    def maxArea(self, height: List[int]) -> int:
        bot = 0
        up = len(height) - 1
        max_water = 0 
        while bot < up:
            amount = (up - bot)*min(height[up], height[bot])
            if amount > max_water:
                max_water = amount
            if height[up] > height[bot]:
                bot += 1
            else:
                up -= 1
        return max_water
