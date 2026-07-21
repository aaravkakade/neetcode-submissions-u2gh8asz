class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #recrusive backtracking
        #r, c, i (word[i] == board[r][c])
        # keep track of visited letters with set - (r, c)
        # 

        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r == ROWS or c == COLS or min(r, c) < 0 or word[i] != board[r][c] or (r, c) in visited:
                return False

            visited.add((r, c))

            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            visited.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0) == True:
                    return True
        return False


        





