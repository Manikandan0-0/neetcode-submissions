class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix = [1] * len(nums)
        product = 1

        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]
        suffix=[1]*len(nums)
        sproduct=1
        for i in range(len(nums)-1,-1,-1):
            suffix[i]=sproduct
            sproduct*=nums[i]
        for i in range(len(nums)):
            res[i]=prefix[i]*suffix[i]
        return res


        