from functools import cache

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        @cache
        def find(total, i):
            if i >= len(nums):
                if total == target:
                    return 1
                return 0
            return find(total + nums[i], i + 1) + find(total - nums[i], i + 1)
        return find(0, 0)