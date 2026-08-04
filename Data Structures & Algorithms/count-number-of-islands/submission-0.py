class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #Iterate through the grid until we run into a 1
        #run a bfs on it and increment counter by 1

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                
                
                for dr, dc in directions:
                    if ((row + dr) in range(ROWS) and (col + dc) in range(COLS) 
                    and grid[row + dr][col + dc] == "1" and (row + dr, col + dc) not in visit):
                        visit.add((row + dr, col + dc))
                        q.append((row + dr, col + dc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands






            



