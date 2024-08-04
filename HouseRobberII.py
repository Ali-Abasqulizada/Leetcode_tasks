class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def find(arr):
            l = r = 0
            for n in arr:
                l, r = r, max(r, l + n)
            return r
        return max(find(nums[1:]), find(nums[:-1]))