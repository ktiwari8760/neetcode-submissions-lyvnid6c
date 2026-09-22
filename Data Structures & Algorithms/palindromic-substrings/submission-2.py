class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            # odd length 
            l , r = i , i

            while (l >= 0 and r < len(s) and s[l] == s[r]):
                # This is a palindrome 
                counter += 1
                l -= 1
                r += 1
            # Even length 
            l , r = i , i+1

            while (l >= 0 and r < len(s) and s[l] == s[r]):
                # This is a palindrome 
                counter += 1
                l -= 1
                r += 1
        return counter
