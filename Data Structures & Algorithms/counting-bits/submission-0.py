class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for n in range(n+1):
            count=0
            while n:
                count+=1
                n = n& (n-1)
            res.append(count)
        return res