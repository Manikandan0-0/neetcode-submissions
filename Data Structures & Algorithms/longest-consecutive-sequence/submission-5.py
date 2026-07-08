class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            if not nums:
                return 0

            s = set(nums)
            res = []

            for num in s:
                if num - 1 not in s:
                    start = num
                    count = 1

                    while start + 1 in s:
                        start += 1
                        count += 1

                    res.append(count)

            return max(res)
            