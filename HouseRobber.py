class Solution:
    def rob(self, nums: list[int]) -> int:
        l, r = 0, 0
        for h in nums:
            l, r = r, max(r, h + l)
        return r