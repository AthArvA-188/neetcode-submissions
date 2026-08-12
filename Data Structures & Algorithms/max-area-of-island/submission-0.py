class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        max_area =float('-inf')
        
        dirs = [[0,1], [-1,0], [0,-1], [1,0]]

        def dfs(i,j):
            if (i<0 or j<0 or i>=ROWS or j>= COLS or grid[i][j]==0):
                return
            nonlocal area
            area+=1
            grid[i][j] =0
            for x,y in dirs:
                dfs(i+x, j+y)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    
                    area =0
                    dfs(i,j)
                    max_area =max(area, max_area)
                    
        return max_area if max_area != float('-inf') else 0
