class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(r , c , visited , prevheight):
            if (r not in range(len(heights))) or (c not in range(len(heights[0]))) or heights[r][c] < prevheight:
                return 
            if (r , c) in visited:
                return
            visited.add((r , c))
            directions = [[1, 0] , [-1 , 0] , [0 , -1] , [0,1]]
            for dr , dc in directions:
                dfs(r+dr , c+dc , visited , heights[r][c])
        pac , ats = set() , set()

        for c in range(len(heights[0])):
            dfs(0 , c , pac , heights[0][c])
            dfs(len(heights)-1 , c , ats , heights[-1][c])
        for r in range(len(heights)):
            dfs(r , 0 , pac , heights[r][0])
            dfs(r , len(heights[0])-1 , ats , heights[r][len(heights[0])-1])
        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pac and (r, c) in ats:
                    res.append([r, c])
        return res