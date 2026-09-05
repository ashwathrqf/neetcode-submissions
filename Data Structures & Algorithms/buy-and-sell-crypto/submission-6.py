class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        def profits(a,b):
            return prices[b]-prices[a]
        profit=0
        for s in range(1,len(prices)):
            profit=max(profit,profits(b,s))
            if prices[s]<prices[b]:
                b=s
        return profit

            

                




        