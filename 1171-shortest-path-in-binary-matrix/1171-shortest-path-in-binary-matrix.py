class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        v=[]
        for i in range(n):
            v.append([False]*n)
        directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        queue=deque([(0,0,1)])
        v[0][0]=True
        while queue:
            r,c,d=queue.popleft()
            if r==n-1 and c==n-1:
                return d
            for dr,dc in directions:
                newr,newc=r+dr,c+dc
                if 0<=newr<n and 0<=newc<n and not v[newr][newc] and grid[newr][newc]==0:
                    v[newr][newc]=True
                    queue.append((newr,newc,d+1))
        return -1



        