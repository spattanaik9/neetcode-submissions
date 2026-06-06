class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows, self.cols, self.word = len(board), len(board[0]), word
        self.dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
        if not word or not board:
            return False

        def dfs(i, j, idx):
            if idx == len(word):
                return True

            if i<0 or i>=self.rows or j<0 or j>=self.cols or board[i][j] == '#' or self.word[idx]!=board[i][j]:
                return False    

            temp = board[i][j]
            board[i][j] = '#'

            for di, dj in self.dirs:
                if dfs(i+di, j+dj, idx+1):
                    return True

            board[i][j] = temp
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False

    


        