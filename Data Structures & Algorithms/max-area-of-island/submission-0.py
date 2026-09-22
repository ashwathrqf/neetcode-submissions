class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area=0
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        def bfs(p,q):
            a=1
            queue=deque([(p,q)])
            grid[p][q]=0
            while queue:
                x,y=queue.popleft()
                for dx,dy in dirs:
                    i=x+dx
                    j=y+dy
                    if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1:
                        queue.append((i,j))
                        grid[i][j]=0
                        a+=1
            return a
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=max(area,bfs(i,j))
        return area
        