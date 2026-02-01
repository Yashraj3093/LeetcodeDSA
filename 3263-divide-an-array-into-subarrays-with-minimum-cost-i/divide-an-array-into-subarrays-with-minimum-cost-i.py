class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = nums[0]
        nums = nums[1:]
        nums.sort()
        return res + nums[0] + nums[1]