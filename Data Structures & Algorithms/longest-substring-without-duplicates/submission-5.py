class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            # Check if character is a duplicate inside the current window
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            # Track the latest index of the character
            char_map[char] = right

            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)

        return max_length
