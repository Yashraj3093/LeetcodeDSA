class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        answer = n
        right = 0
        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            answer = min(answer, n - (right - left))

        return answer