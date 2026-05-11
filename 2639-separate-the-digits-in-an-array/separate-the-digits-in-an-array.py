class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            s = str(n)
            for c in s:
                res.append(int(c))
        
        return res