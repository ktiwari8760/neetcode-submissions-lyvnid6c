class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_ = {value : key for key , value in enumerate(order)}
        print(dict_)
        def compare(word):
            return [dict_[alphabet] for alphabet in word]
        
        return words == sorted(words , key=compare)