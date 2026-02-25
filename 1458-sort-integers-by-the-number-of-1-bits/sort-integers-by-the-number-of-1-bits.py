class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_count(x):
            b = 0
            while x:
                x -= x & -x
                b += 1
            return b

        arr.sort()
        arr.sort(key = lambda x: bit_count(x))
        return arr