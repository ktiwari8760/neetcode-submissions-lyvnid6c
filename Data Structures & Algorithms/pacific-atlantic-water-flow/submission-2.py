class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # We should use dfs

        def dfs(i , j , visited , prevNode):
            if i not in range(len(heights)) or j not in range(len(heights[0])) or heights[i][j] < prevNode:
                return 
            
            if (i , j) in visited:
                return 
            
            visited.add((i , j))
            directions = [[1 , 0] , [0,1] , [-1 , 0] , [0,-1]]

            for dx , dy in directions:
                dfs(i+dx,j+dy , visited , heights[i][j])
            return
        

        pac = set()
        atl = set()

        for i in range(len(heights)):
            dfs(i , 0 , pac , heights[i][0])
            dfs(i , len(heights[0])-1 , atl , heights[i][-1])
        
        for j in range(len(heights[0])):
            dfs(0 , j , pac , heights[0][j])
            dfs(len(heights)-1 , j , atl , heights[-1][j])
        answer = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i , j) in pac and (i, j) in atl:
                    answer.append([i , j])
        return answer