class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        string = ""
        while(right < len(s)):
            if s[right] not in string:
                string += s[right]
            else:
                while((left < right) and (s[right] in string)):
                    string = string[1:]
                    left += 1
                string += s[right]
            max_length = max(max_length , len(string))
            right += 1
        return max_length
                