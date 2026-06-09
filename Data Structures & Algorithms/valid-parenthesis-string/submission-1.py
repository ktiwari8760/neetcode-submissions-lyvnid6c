class Solution:
    def checkValidString(self, s: str) -> bool:
        open_brackets = []
        stars = []

        for i , ele in enumerate(s):
            if ele == "(":
                open_brackets.append((i , ele))
            elif ele == "*":
                stars.append((i , ele))
            else:
                if open_brackets:
                    index , ele = open_brackets.pop()
                elif stars:
                    index , ele = stars.pop()
                else:
                    return False
        while open_brackets and stars:
            index , ele = open_brackets.pop()
            index_str , ele_str = stars.pop()
            if index_str < index:
                return False
        if not open_brackets:
            return True
        return False
