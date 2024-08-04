class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        check = [0] * (amount + 1)
        check[0] = 1
        for c in coins:
            for a in range(c, amount + 1):
                check[a] += check[a - c]