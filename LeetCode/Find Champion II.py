class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champion = -1
        loosers = [False for i in range(n)]

        for edge in edges:
            loosers[edge[1]] = True

        for i in range(n):
            if loosers[i] == False:
                if champion == -1:
                    champion = i
                else:
                    return -1
                  
        return champion

        

                
