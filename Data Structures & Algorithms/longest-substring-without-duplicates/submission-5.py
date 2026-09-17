class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hash = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in hash:
                hash.remove(s[left])
                left += 1
            max_length = max(max_length , right-left+1)
            hash.add(s[right])
        return max_length
        
