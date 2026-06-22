class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def childerens_(number):
            childerens = []
            for i in range(4):
                digit = str((int(number[i])+1) % 10)
                childerens.append(number[:i] + digit + number[i+1:])
                digit = str((int(number[i])-1+10) % 10)
                childerens.append(number[:i] + digit + number[i+1:])
            return childerens
        if "0000" in deadends:
            return -1
        q = deque([("0000" , 0)])
        visited = set(deadends)
        while q:
            number , turns = q.popleft()

            if number == target:
                return turns
            for child in childerens_(number):
                if child not in visited:
                    visited.add(child)
                    q.append((child , turns+1))
        return -1
