class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            i = mid // n
            j = mid % n
            x = matrix[i][j]
            print(mid, i, j)
            if x is target:
                return True
            elif x < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

