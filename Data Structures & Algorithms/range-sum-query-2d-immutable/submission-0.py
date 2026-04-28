class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        i, j = row1, col1
        k, l = row2, col2
        res = 0

        while i <= k:
            # fetch the number at top left corner, then the next number and then the next for that row, then increment the row then start again
            res += sum(self.matrix[i][j:l + 1])
            i += 1


        return res