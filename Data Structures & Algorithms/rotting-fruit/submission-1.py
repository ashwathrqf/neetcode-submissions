from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        rotten=deque([])
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        time=-1
        while rotten:
            time+=1
            for _ in range(len(rotten)):
                x,y=rotten.popleft()
                for dx,dy in dirs:
                    i=x+dx
                    j=y+dy
                    if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1:
                        rotten.append((i,j))
                        grid[i][j]=2
                        fresh-=1
        
        return time if fresh==0 else -1







        
        