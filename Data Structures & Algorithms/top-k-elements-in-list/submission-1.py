class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        for ele in nums:
            dict_[ele] = 1 + dict_.get(ele , 0)
        print(dict_)
        array = [set() for _ in range(len(nums))]
        
        for key , value in dict_.items():
            array[value-1].add(key)
        print(array)
        answer = []
        for ele in array:
            if ele != set():
                answer.extend(list(ele))
        return answer[-k:]