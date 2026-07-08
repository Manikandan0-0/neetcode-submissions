class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p=prices[0]
        max_pf=0
        for price in prices:
            if price<min_p:
                min_p=price
            profit=price-min_p
            if profit>max_pf:
                max_pf=profit
        return max_pf