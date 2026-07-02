class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hash = {i : [] for i in range(n)}
        for ele in edges:
            key , pair = ele
            hash[key].append(pair)
            hash[pair].append(key)
        print(hash)
        seen = set()
        def dfs(node , prev):
            if node in seen:
                return False
            seen.add(node)
            for n in hash[node]:
                if n == prev:
                    continue
                if not dfs(n , node):
                    return False
            return True
        return dfs(0 , -1) and n == len(seen)
        