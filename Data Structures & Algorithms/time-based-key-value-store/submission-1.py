class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[(key , timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key , timestamp) in self.hashmap.keys():
            return self.hashmap[(key , timestamp)]
        else:
            while(key , timestamp) not in self.hashmap.keys():
                timestamp -= 1
            return self.hashmap[(key , timestamp)]