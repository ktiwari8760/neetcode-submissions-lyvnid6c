class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = {}
        for index , ele in enumerate(s):
            if ele in hash.keys():
                min_occurence , max_occurance = hash[ele]
                hash[ele] = [min_occurence , max(max_occurance , index)]
            else:
                hash[ele] = [index , index]
        print(hash)

        values = list(hash.values())
        values.sort(key = lambda x : x[0])
        stack = [values[0]]

        for ele in values[1:]:
            interval = ele
            while(stack and stack[-1][1] > interval[0] and stack[-1][0] < interval[1]):
                a , b = stack.pop()
                interval = [min(interval[0] , a) , max(interval[1] , b)]
            stack.append(interval)
        return [b-a + 1 for a , b in stack]
