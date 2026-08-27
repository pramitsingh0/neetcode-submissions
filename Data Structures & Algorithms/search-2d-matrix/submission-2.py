class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find row, then find column
        t, b = 0, len(matrix) - 1
        row = 0
        while t <= b:
            m = (t + b) // 2

            if matrix[m][0] < target:
                t = m + 1
            elif matrix[m][len(matrix[0]) - 1] > target:
                b = m - 1
            elif matrix[m][0] >= target and matrix[m][len(matrix[0]) - 1] <= target:
                row = m
        # do binary search in row
        print("Row found: ", row)
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
            
