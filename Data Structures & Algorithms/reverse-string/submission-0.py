class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def function(string:str) -> str:
            try:
                left = 0
                right = len(string)-1
                while(left <= right):
                    string[left] , string[right] = string[right] , string[left]
                    left += 1
                    right -= 1
                return string
            except Exception as e:
                print(e)
                return None
        return function(s)