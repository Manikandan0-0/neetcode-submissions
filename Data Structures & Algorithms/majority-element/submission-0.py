class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        top= sorted(freq, key=freq.get, reverse=True)[:1]
        return top[0]