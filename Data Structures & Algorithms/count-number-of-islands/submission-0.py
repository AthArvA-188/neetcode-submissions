class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        x= len(grid)
        y = len(grid[0])
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]

        def dfs(i, j):
            if (i<0 or j<0 or i>=x or j>=y or grid[i][j]=="0"):
                return
            grid[i][j] ="0"
            for dx,dy in dirs:
                dfs(i+dx, j+dy)
        
        for i in range(x):
            for j in range(y):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count
        