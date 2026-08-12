class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time =0
        fresh =0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j] ==1:
                    fresh+=1

        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        while fresh >0 and q:


            for k in range(len(q)):
                i,j = q.popleft()
                for di,dj in dirs:
                    row, col = i+di, j+dj
                    if (row in range(len(grid)) and col in range(len(grid[0]))and grid[row][col]==1):
                        grid[row][col]=2
                        q.append((row, col))
                        fresh -=1
            time+=1
        return time if fresh==0 else -1



