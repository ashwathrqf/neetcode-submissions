class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        profit=0
        for s in range(1,len(prices)):
            if prices[s]<prices[b]:
                b=s
            else:
                profit=max(profit,prices[s]-prices[b])
        return profit

            

                




        