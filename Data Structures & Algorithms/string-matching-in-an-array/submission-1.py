class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        data = [(word , len(word))for word in words]
        data.sort(key = lambda x: x[1] )
        sorted_value = [d[0] for d in data]
        print(sorted_value)
        answer = set()
        for i , word in enumerate(sorted_value):
            for j in range(i+1 , len(words)):
                if word in sorted_value[j]:
                    answer.add(word)
        return list(answer)