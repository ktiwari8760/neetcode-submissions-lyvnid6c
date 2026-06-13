class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = {}
        used = set()

        for i , ele in enumerate(s):
            if ele in hash.keys():
                if hash[ele] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                hash[ele] = t[i]
                used.add(t[i])
        return True