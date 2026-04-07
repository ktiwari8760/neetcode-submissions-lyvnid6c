class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        counter = 0
        while(left <= right):
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right] and counter == 0:
                right -= 1
                counter += 1
            else:
                return False
        return True