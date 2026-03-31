class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        start =0
        end =1
        for i , ele in enumerate(intervals):
            if ele[start] < newInterval[start] and ele[end] < newInterval[start]:
                result.append(ele)
            elif ele[start] > newInterval[end] and ele[end] > newInterval[end]:
                result.append(ele)
            else:
                newInterval = [
                    min(newInterval[start] , ele[start]),
                    max(newInterval[end] , ele[end])
                ]
        result.append(newInterval)
        result.sort(key = lambda x : x[0] )
        return result