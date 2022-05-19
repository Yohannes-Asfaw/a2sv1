    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            sum = 0
            for i in str(n):
                sum += int(i)**2
            n = sum
        return n==1
