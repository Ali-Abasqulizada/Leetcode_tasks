class Solution:
    def canJump(self, nums: list[int]) -> bool:
        index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if index - i <= nums[i]:
                index = i
        return index == 0