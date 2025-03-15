class Solution:
    def sortPeople(self, names, heights):
        dict = {}
        n = len(names)
        result = ['' for i in range(n)]

        for i in range(n):
            dict[heights[i]] = names[i]

        heights.sort(reverse=True)
        for i in range(n):
            result[i] = dict[heights[i]]
        
        return result
    
