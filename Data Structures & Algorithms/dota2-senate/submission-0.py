class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_queue = deque([])
        d_queue = deque([])

        for i , s in enumerate(senate):
            if s == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        while(r_queue and d_queue):
            r_index = r_queue.popleft()
            d_index = d_queue.popleft()
            if r_index < d_index:
                r_queue.append(n+r_index)
            else:
                d_queue.append(n+d_index)
        if r_queue:
            return "Radiant"
        return "Dire"
            
