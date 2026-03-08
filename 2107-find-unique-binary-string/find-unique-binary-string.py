class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        all = set(nums)

        def bt(start, current):
            if start == n:
                if not current in all: return current
                return ''

            for num in ('0', '1'):
                next = bt(start + 1, current + num)
                if next: return next

        return bt(0,'')