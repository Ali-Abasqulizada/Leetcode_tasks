class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = nums[0]
        total = 0
        for e in nums:
            total += e
            ans = max(ans, total)
            if total < 0:
                total = 0
        return ans