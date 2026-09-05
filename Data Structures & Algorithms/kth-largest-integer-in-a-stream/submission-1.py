import heapq 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heapnums=[]
        for num in nums:
            heapq.heappush(self.heapnums,num)
            if len(self.heapnums)>k:
                heapq.heappop(self.heapnums)
        self.k=k

    def add(self, val: int) -> int:
        heapq.heappush(self.heapnums,val)
        if len(self.heapnums)>self.k:
            heapq.heappop(self.heapnums)
        return self.heapnums[0]



        
