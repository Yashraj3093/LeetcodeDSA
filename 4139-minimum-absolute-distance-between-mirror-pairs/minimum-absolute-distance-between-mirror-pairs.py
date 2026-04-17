class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        rev = {}
        result = inf

        for i, n in enumerate(nums):
            if n in rev: result = min(result, i - rev[n])
            r = int(str(n)[::-1])
            rev[r] = i

        return result if result != inf else -1