class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for ele in strs:
            s += str(len(ele))
            s += "#"
            s += ele
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        index = 0
        answer = []
        while(index < len(s)):
            if s[index].isdigit():
                length = ""
                while s[index].isdigit():
                    length += s[index]
                    index += 1
                length = int(length)
                answer.append(s[index+1 : index+1+length])
                index += 1 + length
            else:
                index += 1
        return answer