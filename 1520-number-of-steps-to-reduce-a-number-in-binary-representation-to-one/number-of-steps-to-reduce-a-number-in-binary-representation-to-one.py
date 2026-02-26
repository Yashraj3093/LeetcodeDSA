class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        carry = 0
        result = 0

        for i in range(n - 1, 0 , -1):
            current = int(s[i]) + carry
            if current == 1:
                result += 2
                carry = 1
            else:
                result += 1
        
        return result + carry