class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = collections.deque()

        # def bfs(r,c):
        #     if (r<0 or c<0 or c>=cols or r >= rows or grid[r][c]==0 or (r,c) in visited):
        #         return
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] ==1:
                    fresh+=1
                
        dirs = [[0,-1], [1,0], [-1,0], [0,1]]

        while q and fresh>0:
            for k in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    row, col = r+dr, c+dc
                    if (row in range(rows) and col in range(cols) and grid[row][col]==1):
                        grid[row][col] =2
                        q.append((row, col))
                        fresh -=1
            time+=1
        return time if fresh==0 else -1


                




