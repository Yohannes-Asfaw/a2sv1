    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        x=0
        for i in range(len(piles)//3):
            sum+=piles[-2-x]
            x+=2

        return sum
