class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0 for i in range(27)]

        for ele in s:
            index = ord(ele.lower()) - ord("a")
            arr1[index] += 1
        
        for ele in t:
            index = ord(ele.lower()) - ord("a")
            arr1[index] -= 1
        return all(ele == 0 for ele in arr1)