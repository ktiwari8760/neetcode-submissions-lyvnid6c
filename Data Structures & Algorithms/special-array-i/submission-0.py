class Solution:
    def isArraySpecial(self, arr: List[int]) -> bool:
        
        if len(arr) == 1:
            return True
        last_ele = None
        for i in range(len(arr)):
            eve_odd = "even" if arr[i] % 2 == 0 else "odd"
            if not last_ele:
                last_ele = eve_odd
            elif eve_odd == last_ele:
                return False
            else:
                last_ele = eve_odd
        return True