class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        if nums[left]==target:
            return left
        while(left<=right):
            if nums[left] == target:
                return left
            elif nums[right]== target:
                return right
            else:
                left+=1
                right-=1
        return -1