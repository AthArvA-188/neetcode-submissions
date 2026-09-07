class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROW, COL = len(grid), len(grid[0])
        
        visit = set()

        def dfs(i, j):
            if i<0 or i>=ROW or j<0 or j>=COL or (i,j) in visit or grid[i][j]=="0":
                return
            visit.add((i, j))
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i-1, j)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and (i,j) not in visit:
                    res +=1
                    dfs(i,j)
        return res

