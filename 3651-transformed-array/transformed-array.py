class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i,v in enumerate(nums):
            result.append(nums[(i + v) % n])

        return result
