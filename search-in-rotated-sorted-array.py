class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        #find row to narrown target
        while top <= bot:
            row = (top + bot)//2
            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break 
        
        l, r = 0, len(matrix[0]) - 1

      #simply binary search to find target in row 
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False
        


if __name__ == "__main__":
  pass 
