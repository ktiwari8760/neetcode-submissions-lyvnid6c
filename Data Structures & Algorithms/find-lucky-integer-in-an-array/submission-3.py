class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()

        counter = 0
        max_lucky = -1
        for i in range(len(arr)):
            print(arr[i])
            if arr[i] == arr[i-1]:
                counter += 1
            else:
                if counter == arr[i-1]:
                    max_lucky = max(max_lucky , arr[i-1])
                counter = 1
        print("counter" , counter)
        if counter == arr[i]:
            max_lucky = max(max_lucky , arr[i-1])
        return max_lucky


