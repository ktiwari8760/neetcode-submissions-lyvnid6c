class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []

        def helper(index , string):
            if len(string) == len(digits):
                result.append(string)
                return
            if index > len(digits)-1:
                return
            for ele in phone[digits[index]]:
                helper(index+1 , string + ele)
                helper(index+1 , string)
            
        helper(0 , "")
        return result
            





