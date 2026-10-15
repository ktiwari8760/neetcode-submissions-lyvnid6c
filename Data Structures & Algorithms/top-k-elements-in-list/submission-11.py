class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We approach this problem using heap
        """
        Time Complexity : O(N)
        Space Complexity : O(N)
        """
        hash_freq = Counter(nums) # This gives me the freq for the nums

        heap = []
        heapq.heapify(heap)
        # This is pushed in reverse to get the max on top
        for key , value in hash_freq.items():
            heapq.heappush(heap , (-value , key))
        answer = []
        while k: # We retrieve k elements from the heap
            freq , value = heapq.heappop(heap)
            answer.append(value)
            k -= 1
        return answer