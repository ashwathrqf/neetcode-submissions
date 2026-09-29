import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest=[]
        for pt in points:
            d=pt[0]**2+pt[1]**2
            heapq.heappush(closest,(-d,pt))
            if len(closest)>k:
                heapq.heappop(closest)
        res=[]
        for _,pt in closest:
            res.append(pt)
        return res