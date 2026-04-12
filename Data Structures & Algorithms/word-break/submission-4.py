class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # O(1) lookup
        hash = {}
        def df(index):
            if index == len(s):
                return True
            if index in hash:
                return hash[index]
            hash[index] = False
            for i in range(index, len(s)):
                substring = s[index:i+1]
                
                if substring in wordSet:
                    if df(i + 1):   # move forward
                        hash[index] = True
                        return True
            
            return False
        
        return df(0)