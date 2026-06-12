class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        hash = {}
        for idx , pattern in enumerate(pattern):
            if pattern in hash.keys():
                if hash[pattern] != s[idx]:
                    return False
            elif s[idx] in hash.values():
                return False
            else:
                hash[pattern] = s[idx]
        return True
