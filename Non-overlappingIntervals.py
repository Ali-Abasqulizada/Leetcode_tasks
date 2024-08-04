class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda x : (x[0], x[1]))
        check = intervals[0][1]
        for l, r in intervals[1:]:
            if check <= l:
                check = r
            else:
                ans += 1
                check = min(check, r)
        return ans