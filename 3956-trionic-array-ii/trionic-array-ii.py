class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        res = -inf 
        i = 0

        while i < n:
            j = i + 1
            while j < n and nums[j] > nums[j - 1]:
                j += 1
            p = j - 1

            if p == i:
                i += 1
                continue

            curr = nums[p] + nums[p - 1]

            while j < n and nums[j] < nums[j - 1]:
                curr += nums[j]
                j += 1

            q = j - 1

            if p == q or q == n - 1 or (q < n - 1 and nums[q] == nums[j]):
                i = q
                continue

            curr += nums[j]
            j += 1

            acc = 0
            mx = 0
            while j < n and nums[j] > nums[j - 1]:
                acc += nums[j]
                mx = max(mx, acc)
                j += 1
            curr += mx

            acc = 0
            mx = 0
            jj = p - 2
            while jj >= 0 and nums[jj] < nums[jj + 1]:
                acc += nums[jj]
                mx = max(mx, acc)
                jj -= 1
            curr += mx

            res = max(res,curr)
            i = q

        return res