class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL  = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def bfs(i,j):
            if i<0 or i>=ROW or j<0 or j>=COL or (i,j) in visit or grid[i][j]== -1:
                return
            visit.add((i,j))
            q.append([i,j])

        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] ==0:
                    q.append([i,j])
                    visit.add((i,j))
        dist =0
        while q:
            for x in range(len(q)):

                i,j = q.popleft()
                grid[i][j] = dist
                bfs(i+1, j)
                bfs(i, j-1)
                bfs(i, j+1)
                bfs(i-1, j)
            dist+=1
        
            