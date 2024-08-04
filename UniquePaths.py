class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        check = [[1] * n for _ in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                check[i][j] = check[i + 1][j] + check[i][j + 1]
        return check[0][0]