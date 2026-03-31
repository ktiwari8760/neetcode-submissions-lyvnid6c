class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)-1
        while(right < len(s2)):
            string1 = sorted(s1)
            string2 = sorted(s2[left:right+1])
            print(string1 , string2)
            if string1 == string2:
                return True
            left+= 1
            right += 1
        return False