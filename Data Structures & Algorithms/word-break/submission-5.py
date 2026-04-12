class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hash = {}
        def function(index):
            if index == len(s):
                return True
            if index in hash:
                return hash[index]
            hash[index] = False

            for i in range(index , len(s)):
                substring = s[index : i+1]
                if substring in wordDict:
                    # I tak ka toh hai aage ka check karo 
                    if function(i+1):
                        hash[index] = True
                        return True
            return False
        return function(0)
