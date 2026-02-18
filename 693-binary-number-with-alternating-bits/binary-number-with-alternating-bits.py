class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        previous = -1
        while n: 
            if n % 2 == previous: return False
            previous = n % 2
            n >>= 1

        return True 