class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()

        left = 0
        right = 0
        max_length = 0
        while(right < len(s)):
            while s[right] in hash:
                hash.remove(s[left])
                left += 1
            hash.add(s[right])
            right += 1
            max_length = max(max_length , right-left)
        return max_length