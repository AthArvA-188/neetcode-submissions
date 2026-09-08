class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])

        visit = set()
        marea = 0
        def dfs(i,j):
            if i>=row or i<0 or j<0 or j >= col or (i,j) in visit or grid[i][j]==0:
                return 0
            visit.add((i,j))
            carea =1
            carea +=(dfs(i+1, j))
            carea +=(dfs(i-1, j))
            carea +=(dfs(i, j-1))
            carea +=(dfs(i, j+1)
            )
            return carea
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] ==1 and (i,j) not in visit:
                    carea = dfs(i,j)
                    marea = max(marea, carea)

        return marea