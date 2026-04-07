class Solution:

    def encode(self, strs: List[str]) -> str:
        string_ = ""
        for ele in strs:
            length = len(ele)
            string_ += f"{length}#{ele}"
        print(string_)
        return string_
    def decode(self, s: str) -> List[str]:
        listing = []
        print(s)
        for i , ele in enumerate(s):
            if ele.isdigit() and i != len(s)-1 and s[i+1] == "#":
                print(s[i+2:i+2+int(ele)] , i)
                listing.append(s[i+2:i+2+int(ele)])
        return listing

        