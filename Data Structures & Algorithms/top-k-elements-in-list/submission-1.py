from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        freq=Counter(nums)
        result=[key for key,count in freq.most_common(k)]
        return result
    
        