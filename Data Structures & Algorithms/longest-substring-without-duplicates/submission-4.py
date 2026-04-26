class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_length = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in window:
                window.add(s[i])
            else:
                while s[i] in window:
                    window.remove(s[l])
                    l += 1
                window.add(s[i])
            max_length = max(max_length , len(window))
        return max_length