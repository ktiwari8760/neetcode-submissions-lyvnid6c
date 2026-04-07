class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        counter = 0
        def function(index , substring):
            nonlocal counter
            print(counter , substring)
            if substring in wordDict:
                counter += len(substring)
                substring = ""
            if index > len(s)-1:
                return True
            function(index + 1 , substring + s[index])
        function(0 , "")
        print(counter)

        return counter == len(s)