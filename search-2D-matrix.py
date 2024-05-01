class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2
            #target is greater than the largest element in the row
            if matrix[row][-1] < target:
                top = row + 1
            #target is smaller than the smallest element in the row
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                #target could be within this row
                break

        #binary search on the row
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
