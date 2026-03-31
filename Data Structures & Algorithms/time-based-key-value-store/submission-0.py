class TimeMap:

    def __init__(self):
        self.dict1 = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict1:
            self.dict1[key] = {}
        if timestamp not in self.dict1[key]:
            self.dict1[key][timestamp] = []
        self.dict1[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict1:
            return ""
        
        # Find the largest timestamp <= requested timestamp
        seen = -1  # No valid timestamp found yet
        for time in self.dict1[key]:
            if time <= timestamp:
                seen = max(seen, time)
        
        if seen == -1:
            return ""
        
        # Return the latest value associated with the most recent timestamp
        return self.dict1[key][seen][-1]  # Return the last value for the largest timestamp
