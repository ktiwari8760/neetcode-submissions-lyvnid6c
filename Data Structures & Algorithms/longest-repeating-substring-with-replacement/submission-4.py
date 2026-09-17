class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = {}
        max_freq = 0
        left = 0
        max_length = 0

        for right in range(len(s)):
            hash[s[right]] = hash.get(s[right] , 0) + 1
            max_freq = max(max_freq , hash[s[right]])

            while (right-left+1) - max_freq > k:
                hash[s[left]] -= 1
                left += 1
            
            max_length = max(max_length , right-left+1)
        return max_length