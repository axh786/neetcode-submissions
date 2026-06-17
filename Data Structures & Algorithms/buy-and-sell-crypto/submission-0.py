class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf, l, r = 0, 0, 1
        if len(prices) <= 1:
            return maxProf
        
        for index in range(len(prices) - 1):
            if prices[r] - prices[l] > maxProf:
                maxProf = prices[r] - prices[l]
            
            if prices[r] - prices[l] < 0:
                l = r
            
            r += 1

        return maxProf
        