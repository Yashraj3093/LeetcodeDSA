class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)

        expected = 1
        for i in range(n):
            if nums[i] != expected: return False
            if i < n - 2: expected += 1

        return n == nums[-1] + 1