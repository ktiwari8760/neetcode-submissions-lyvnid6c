class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        left1 = 0
        left2 = 0

        max_loop_range = min(len(word1) , len(word2))
        while(left1 < max_loop_range and left2 <max_loop_range):
            string += word1[left1]
            string += word2[left2]
            left1 += 1
            left2 += 1
        while(left1 < len(word1)):
            string += word1[left1]
            left1 += 1

        while(left2 < len(word2)):
            string += word2[left2]
            left2 += 1
        return string