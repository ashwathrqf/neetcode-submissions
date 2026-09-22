from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        count=0
        def bfs(p,q):
            queue=deque([(p,q)])
            grid[p][q]="0"
            while queue:
                a,b=queue.popleft()
                for x,y in dirs:
                    i=a+x
                    j=b+y
                    if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=="1":
                        queue.append((i,j))
                        grid[i][j]="0"
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    bfs(i,j)
                    count+=1
        return count







        