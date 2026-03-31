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

        def helper(index , substring):
            if index == len(digits):
                result.append(substring)
                return
            letters = phone[digits[index]]

            for letter in letters:
                helper(index+1 , substring+letter)
        helper(0 , "")
        return result
