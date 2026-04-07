class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def function(index):
            if index == len(s):
                return True
            
            for word in wordDict:
                if s.startswith(word , index):
                    if function(index + len(word)):
                        return True
            return False
        
        return function(0)