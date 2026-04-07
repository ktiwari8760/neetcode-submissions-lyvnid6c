class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26

        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1
        
        # Compare
        if arr1 == arr2:
            return True
        left = 0
        for right in range(len(s1) , len(s2)):
            arr2[ord(s2[right]) - ord('a')] += 1
            arr2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            if arr1 == arr2:
                return True
        return False
