from functools import cache

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        @cache
        def find(total):
            if total == target:
                return 1
            elif total > target:
                return 0
            ans = 0
            for i in nums:
                ans += find(total + i)
            return ans
        return find(0)