class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid = True
        # Check horizontal
        for row in board:
            track_dict = {}
            for cell in row:
                if cell == ".":
                    continue
                elif cell in track_dict:
                    return False
                else:
                    track_dict[cell] = True
        # Check vertical
        for col_idx in range(9):
            track_dict = {}
            for row_idx in range(9):
                value = board[row_idx][col_idx]
                if value == ".":
                    continue
                elif value in track_dict:
                    return False
                else:
                    track_dict[value] = True
        # Check squares
        for col_mul in range(3):
            for row_mul in range(3):
                track_dict = {}
                for i in range(3):
                    for j in range(3):
                        value = board[col_mul * 3 + i][row_mul * 3 + j]
                        if value == ".":
                            continue
                        elif value in track_dict:
                            return False
                        else:
                            track_dict[value] = True
        return is_valid