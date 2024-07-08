class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        check = {}
        for i in nums:
            check[i] = check.get(i, 0) + 1
        stack = []
        for i in check:
            stack.append((check[i], i))
        stack.sort(key = lambda x : -x[0])
        ans = []
        for i in range(k):
            ans.append(stack[i][1])
        return ans