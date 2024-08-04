class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key = lambda x : (x[1], x[0]))
        check = pairs[0][1]
        ans = 1
        for l, r in pairs[1:]:
            if check < l:
                ans += 1
                check = r
            else:
                check = min(check, r)
        return ans 