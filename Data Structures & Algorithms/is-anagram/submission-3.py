class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26

        for ele in s:
            index = ord(ele) - ord('a')
            arr[index] += 1
        for ele in t:
            index = ord(ele) - ord('a')
            arr[index] -= 1
        for ele in arr:
            if ele != 0:
                return False
        return True