class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        prev = [i - 1 for i in range(len(nums))]
        nxt = [i + 1 for i in range(len(nums))]
        nxt[-1] = -1
        q = []
        unordered = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                unordered += 1
            heappush(q, (nums[i - 1] + nums[i], i))

        res = 0

        while unordered != 0:
            total, r = heappop(q)
            l = prev[r]
            if l == -1 or nums[l] + nums[r] != total:
                continue
            nxt[l] = nxt[r]
            prev[nxt[r]] = l

            if nums[l] > nums[r]:
                unordered -= 1
            left = prev[l]
            right = nxt[r]

            if left != -1:
                unordered += (nums[left] > total) - (nums[left] > nums[l])
                heappush(q, (nums[left] + total, l))

            if right != -1:
                unordered += (total > nums[right]) - (nums[r] > nums[right])
                heappush(q, (nums[right] + total, right))
            nums[l] = total
            nums[r] = inf
            res += 1

        return res



