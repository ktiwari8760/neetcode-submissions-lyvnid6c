class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        hash = {value : key for key , value in enumerate(order)}


        for i in range(len(words)-1):
            w1 , w2 = words[i] , words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    # means w2 is the prefix of w1 and it has to come first
                    return False
                if w1[j] != w2[j]:
                    if hash[w1[j]] > hash[w2[j]]:
                        return False
                    break
        return True
