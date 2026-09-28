class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        currmin,currmax=1,1
        for n in nums:
            if n==0:
                currmax,currmin=1,1
                continue
            temp= currmax*n
            currmax=max(n*currmax,n*currmin,n)
            currmin=min(temp,n*currmin,n)
            res=max(res,currmax)
        return res