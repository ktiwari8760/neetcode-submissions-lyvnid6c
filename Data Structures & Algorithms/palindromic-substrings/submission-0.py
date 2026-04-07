class Solution:
    def countSubstrings(self, s: str) -> int:
        def check_palindrome(string):
            return string == string[::-1]
        counter = 0
        for i in range(len(s)):
            for j in range(i , len(s)):
                print(s[i:j+1])
                counter += int(check_palindrome(s[i:j+1]))
        return counter
