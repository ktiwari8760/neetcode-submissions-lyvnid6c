class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap.keys():
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp , value))
    def get(self, key: str, timestamp: int) -> str:

        arr = self.hashmap.get(key , [])
        left = 0
        right = len(arr)-1
        possible_answer = ""
        while(left<=right):
            mid = (left+right)//2
            if arr[mid][0] <= timestamp:
                possible_answer = arr[mid][1]
                left = mid+1
            else:
                right = mid-1
        return possible_answer
        
