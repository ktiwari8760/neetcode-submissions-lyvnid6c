class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = Counter(nums)
        arr = [[] for _ in range(len(nums))] 
        for key , value in hash.items():
            arr[value-1].append(key)
        
        answer = []
        for ele in arr[::-1]:
            if not ele:
                continue
            answer.extend(ele)
        return answer[:k]
