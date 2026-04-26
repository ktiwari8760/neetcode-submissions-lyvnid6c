class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        max_length = 0
        for i in range(len(s)):
            if s[i] not in window:
                window.append(s[i])
            else:
                while s[i] in window:
                    window.pop(0)
                window.append(s[i])
            max_length = max(max_length , len(window))
        return max_length