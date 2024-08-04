class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        check = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    check[i] = max(check[i], 1 + check[j])
        return max(check)