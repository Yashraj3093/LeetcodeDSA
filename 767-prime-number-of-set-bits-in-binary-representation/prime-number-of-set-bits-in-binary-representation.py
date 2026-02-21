class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isSmallPrime(x):
            return x in {2,3,5,7,11,13,17,19}

        answer = 0
        for x in range(left, right + 1):
            if isSmallPrime(x.bit_count()):
                answer += 1
        
        return answer