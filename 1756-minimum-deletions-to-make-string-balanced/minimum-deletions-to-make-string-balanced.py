class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        result = 0
        for c in s:
            if c == 'b' : b += 1
            else: result = min(result + 1,b)

        return result 