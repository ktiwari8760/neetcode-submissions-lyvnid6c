class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check_permutation(string1 , string2):
            arr1 = [0] * 26
            arr2 = [0] * 26
            for ele in string1:
                index = ord(ele) - ord('a')
                arr1[index] += 1
            for ele in string2:
                index = ord(ele) - ord('a')
                arr2[index] += 1
            return arr1 == arr2
            
        left = 0
        right = len(s1)-1
        while(right < len(s2)):
            string1 = s1
            string2 = s2[left:right+1]
            print(string1 , string2)
            if check_permutation(string1 , string2):
                return True
            left+= 1
            right += 1
        return False