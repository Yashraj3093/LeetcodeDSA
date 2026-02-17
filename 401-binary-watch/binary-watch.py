class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        def bit_count(n):
            result = 0
            while n: 
                result += n % 2 == 1
                n //= 2
            return result 

        for h in range(12):
            for m in range(60):
                if bit_count(h) + bit_count(m) == turnedOn:
                    m = str(m)
                    m = m if len(m) > 1 else '0' + m
                    result.append(str(h) + ':' + m)

        return result 