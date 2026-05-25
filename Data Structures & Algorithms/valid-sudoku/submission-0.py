class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue

                if (cell in row[i] or 
                    cell in col[j] or   
                    cell in square[(i//3, j//3)]):
                    return False

                row[i].add(cell)
                col[j].add(cell) 
                square[(i//3, j//3)].add(cell)   

        return True        
        