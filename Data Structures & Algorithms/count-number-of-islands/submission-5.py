class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res =0
        ROW , COL = len(grid), len(grid[0])

        visit = set()

        def dfs(r,c):
            if r in range(ROW) and c in range(COL) and (r,c) not in visit and grid[r][c]=="1":
                visit.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            else:
                return
            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in visit:
                    
                    dfs(r,c)
                    res +=1
        dfs(0,0)
        return res

