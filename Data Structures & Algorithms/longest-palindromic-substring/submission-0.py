class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(sub):
            return sub == sub[::-1]

        answer = ""
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(answer):
                    answer = substring

        return answer