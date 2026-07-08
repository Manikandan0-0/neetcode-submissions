class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        l=0
        max_len=0
        for r in range(len(s)):
            if s[r] in dic:
                if dic[s[r]] >= l:
                    l=dic[s[r]]+1
            max_len = max(max_len, r - l + 1)
            dic[s[r]]=r
        return max_len