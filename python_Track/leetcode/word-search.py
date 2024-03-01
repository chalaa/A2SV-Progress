class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.flag = False
        self._set = set()
        self.s = ""
        n = len(board) 
        m = len(board[0])
        def backtrack(row,col,ind):
            if ind == len(word):
                return True
            if row >= n or row < 0 or col >= m or col < 0:
                return False
            if board[row][col] != word[ind]:
                return False
            if (row,col) in self._set:
                return False

            self._set.add((row,col))
            res = (backtrack(row+1,col,ind+1) or
            backtrack(row-1,col,ind+1) or
            backtrack(row,col+1,ind+1) or
            backtrack(row,col-1,ind+1))
            self._set.remove((row,col))
            return res

        for i in range(n):
            for j in range(m):
                if backtrack(i,j,0):
                    return True
        return False
                    