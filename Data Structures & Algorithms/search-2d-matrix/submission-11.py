class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_idx = 0
        btm_idx = len(matrix) - 1
        while top_idx <= btm_idx:
            row_idx = (top_idx + btm_idx) // 2
            if matrix[row_idx][0] == target:
                return True
            elif matrix[row_idx][0] > target:
                btm_idx = row_idx - 1
            elif matrix[row_idx][-1] < target:
                top_idx = row_idx + 1
            else:
                break
        if not (top_idx <= btm_idx):
            return False
        row_idx = (top_idx + btm_idx) // 2
        left_idx = 0
        right_idx = len(matrix[row_idx]) - 1
        while left_idx <= right_idx:
            col_idx = (left_idx + right_idx) // 2
            if matrix[row_idx][col_idx] == target:
                return True
            elif matrix[row_idx][col_idx] > target:
                right_idx = col_idx - 1
            else:
                left_idx = col_idx + 1
        return False