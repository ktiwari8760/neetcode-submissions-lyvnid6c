class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        window = set()
        for right in range(len(s)):
            ele = s[right]

            while ele in window:
                window.remove(s[left])
                left += 1

            max_length = max(max_length , right-left+1)
            window.add(s[right])
        return max_length

        