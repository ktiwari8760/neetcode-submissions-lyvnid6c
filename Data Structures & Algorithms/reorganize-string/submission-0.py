class Solution:
    def reorganizeString(self, s: str) -> str:
        map = {}
        result = []
        for ele in s:
            if ele in map.keys():
                map[ele] += 1
            else:
                map[ele] = 1
        heap = [(-v , k) for k , v in map.items()]
        heapq.heapify(heap)
        prev = (0 , "")
        while(heap):
            count , ch = heapq.heappop(heap)
            result.append(ch)
            count += 1
            if prev[0] < 0:
                heapq.heappush(heap , prev)
            prev = (count , ch)
        if len(result) != len(s):
            return ""
        return "".join(result)