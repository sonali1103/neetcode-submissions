class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top_row = 0
        bot_row = ROWS - 1
        target_row = 0
        while top_row <= bot_row:
            mid_row = (top_row + bot_row) // 2
            if target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            else:
                target_row = mid_row
                break
        if top_row > bot_row:
            return False
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[target_row][mid]:
                r = mid - 1
            elif target > matrix[target_row][mid]:
                l = mid + 1
            else:
                return True
        return False



        