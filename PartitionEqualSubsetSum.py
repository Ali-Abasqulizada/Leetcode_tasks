class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        total //= 2
        ans = set()
        ans.add(0)
        for i in range(len(nums) - 1, -1, -1):
            check = set()
            for n in ans:
                check.add(n)
                check.add(n + nums[i])
            ans = check
        return True if total in ans else False