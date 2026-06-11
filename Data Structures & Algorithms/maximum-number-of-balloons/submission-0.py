class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash = Counter(text)
        hash2 = Counter("balloon")
        print(hash)
        print(hash2)
        answer = []
        for ele in "balloon":
            freq = hash2[ele]
            freq_text = hash.get(ele , 0)
            accomodate = freq_text // freq if freq !=0 else 0
            answer.append(accomodate)
        return min(answer)

