class Solution:
    def frequencySort(self, s: str) -> str:
        check = {}
        for i in s:
            check[i] = check.get(i, 0) + 1
        stack = []
        for i in check:
            stack.append((check[i], i))
        stack.sort(key = lambda x : -x[0])
        ans = ""
        for i in stack:
            ans += i[1] * i[0]
        return ans