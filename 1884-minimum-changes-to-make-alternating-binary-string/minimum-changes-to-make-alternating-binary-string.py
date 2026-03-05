class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = '0'
        current = 0

        for c in s: 
            if c != t: current += 1
            t = '1' if t == '0' else '0'

        result = current
        t = '1'
        current = 0
        for c in s:
            if c != t: current += 1
            t = '1' if t == '0' else '0'

        return min(result,current)