class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        previous = 0
        total = sum(nums)

        for i in range(n):
            previous += nums[i] * i
        
        result = previous
        for i in range(n - 1, 0, -1):
            previous = previous + (total - nums[i]) - (n - 1) * nums[i]
            result = max(result, previous)

        return result