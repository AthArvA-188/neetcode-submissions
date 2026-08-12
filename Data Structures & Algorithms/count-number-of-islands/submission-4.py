class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0 
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(i,j):
            if i<0 or j<0 or j>=cols or i>= rows or grid[i][j]=="0" or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)


            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j)
                    count +=1
        return count            

