    def getDescentPeriods(self, prices: List[int]) -> int:
        result = count = 1
        for i in range(1,len(prices)):
            if prices[i] == prices[i-1] - 1: count += 1
            else: count = 1
            result += count
        return result
