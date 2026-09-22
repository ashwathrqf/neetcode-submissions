from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        count=0
        visited=set()
        def bfs(p,q,v):
            v.add((p,q))
            queue=deque([(p,q)])
            while queue:
                a,b=queue.popleft()
                for x,y in dirs:
                    i=a+x
                    j=b+y
                    if 0<=i<len(grid) and 0<=j<len(grid[0]):
                        if grid[i][j]=='1' and (i,j) not in v:
                            queue.append((i,j))
                            v.add((i,j))
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in visited:
                    bfs(i,j,visited)
                    count+=1
        return count







        