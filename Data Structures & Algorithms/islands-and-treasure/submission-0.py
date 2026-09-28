from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    treasure.append((i,j))
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        def bfs(a,b):
            q=deque([(a,b)])
            while q:
                x,y=q.popleft()
                for dx,dy in dirs:
                    i=x+dx
                    j=y+dy
                    if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]!=0 and grid[i][j]>1+grid[x][y]:
                        grid[i][j]=1+grid[x][y]
                        q.append((i,j))
            return
        for i,j in treasure:
            bfs(i,j)
        return  
        