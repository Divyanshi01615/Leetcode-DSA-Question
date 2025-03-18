class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island=0
        r=len(grid)
        c=len(grid[0])
        def bfs(i,j):
            queue=deque([(i,j)])
            grid[i][j]='-1'
            directions=[(-1,0),(1,0),(0,1),(0,-1)]
            while queue:
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr, c+dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=='1':
                        queue.append((nr,nc))
                        grid[nr][nc]='-1'
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    island+=1
                    bfs(i,j)
        return island

        