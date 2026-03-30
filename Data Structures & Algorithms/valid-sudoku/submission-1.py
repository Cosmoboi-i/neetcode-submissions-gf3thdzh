class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            count = {}
            for cell in row:
                if cell == ".":
                    continue
                count[cell] = 1 + count.get(cell, 0)
                if count[cell] > 1:
                    print(cell)
                    return False
            
        for i in range(9):
            count = {}
            for row in board:
                cell = row[i]
                if cell == ".":
                    continue
                count[cell] = 1 + count.get(cell, 0)
                if count[cell] > 1:
                    print(cell, i)
                    return False
        
        for a in range(3):
            for b in range(3):
                count = {}
                for i in range(3):
                    for j in range(3):
                        cell = board[a*3 + i][b*3 + j]
                        if cell == ".":
                            continue
                        count[cell] = 1 + count.get(cell, 0)
                        if count[cell] > 1:
                            print(cell, i, j)
                            return False
        
        return True


