class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        i = 1
        while i < n and nums[i] > nums[i - 1]: i += 1

        p = i - 1
        if p == 0: return False

        while i < n and nums[i] < nums[i - 1]: i += 1

        q = i - 1
        if q == p: return False

        while i < n and nums[i] > nums[i - 1]: i += 1

        if i - 1 == q or i < n: return False
        return True 