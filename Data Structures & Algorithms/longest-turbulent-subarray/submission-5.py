class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        def check_turbulence(subarray):
            if len(subarray) <= 1:
                return True
            if len(subarray) == 2:
                return subarray[0] != subarray[1]
            for i in range(1, len(subarray) - 1):
                peak   = subarray[i-1] < subarray[i] > subarray[i+1]
                valley = subarray[i-1] > subarray[i] < subarray[i+1]
                if not (peak or valley):
                    return False
            return True

        start = 0
        max_length = 1

        for end in range(len(arr)):
            subarray = arr[start:end+1]
            if not check_turbulence(subarray):
                if arr[end] == arr[end-1]:
                    start = end        # equal → can't salvage previous element
                else:
                    start = end - 1    # direction broke → salvage last element
            max_length = max(max_length, end - start + 1)

        return max_length