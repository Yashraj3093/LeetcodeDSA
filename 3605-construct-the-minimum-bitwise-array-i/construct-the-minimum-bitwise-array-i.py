class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # result = []
        # for num in nums:
        #     original = num 
        #     candidate = -1
        #     for j in range(1, original):
        #         if (j | (j + 1)) == original:
        #             candidate = j
        #             break
        #     result.append(candidate)
        # return result 

        n = len(nums)
        result = []

        for i in range(n):
            current = -1
            for c in range(nums[i]):
                if c | (c + 1) == nums[i]:
                    current = c
                    break
            result.append(current)
        
        return result