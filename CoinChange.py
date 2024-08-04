class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        check = [float("inf")] * (amount + 1)
        check[0] = 0
        for c in coins:
            for a in range(c, amount + 1):
                check[a] = min(check[a], check[a - c] + 1)
        return check[-1] if check[-1] != float("inf") else -1