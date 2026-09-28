class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        alist=[[] for _ in range(n)]
        for i,j in edges:
            alist[i].append(j)
            alist[j].append(i)
        visited=set()
        def dfs(a):
            visited.add(a)
            for i in alist[a]:
                if i not in visited:
                    dfs(i)
            return
        count=0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count




        