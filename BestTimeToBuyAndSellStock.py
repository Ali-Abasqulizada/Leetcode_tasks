class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            diff = prices[i] - buy
            ans = max(ans, diff)
            buy = min(buy, prices[i])
        return ans