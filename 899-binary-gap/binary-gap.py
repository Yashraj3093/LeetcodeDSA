class Solution:
    def binaryGap(self, n: int) -> int:
        result = 0
        position = 0
        last = -1

        while n:
            if n % 2 == 1:
                if last != -1: result = max(result, position - last)
                last = position

            n >>= 1
            position += 1
        
        return result 