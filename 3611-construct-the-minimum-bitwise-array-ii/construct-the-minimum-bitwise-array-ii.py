class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            result = -1
            position = 0
            while(nums[i] & (1 << position)) != 0:
                result = nums[i] ^ (1 << position)
                position += 1
            nums[i] = result

        return nums