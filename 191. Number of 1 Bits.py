    def hammingWeight(self, n: int) -> int:
        count = 0
        for num in str(bin(n)):
            if num == '1':
                count += 1
        return count
