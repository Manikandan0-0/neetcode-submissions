class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        max_freq=0
        max_length=0
        freq={}
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            window_length = r - l + 1
            max_freq = max(max_freq, freq[s[r]])
            replacements = window_length - max_freq
            if replacements>k:
                freq[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length