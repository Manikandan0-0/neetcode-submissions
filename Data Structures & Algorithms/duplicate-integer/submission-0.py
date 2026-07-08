class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for nums in nums:
            if nums in seen:
                return True
            seen.add(nums)
        return False
        