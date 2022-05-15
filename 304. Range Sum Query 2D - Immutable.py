class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0] + row for row in matrix]
        for i in range(len(self.sums)):
            for j in range(1, len(self.sums[0])):
                self.sums[i][j] = self.sums[i][j-1] + self.sums[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2+1):
            total += self.sums[i][col2+1] - self.sums[i][col1]
        return total
