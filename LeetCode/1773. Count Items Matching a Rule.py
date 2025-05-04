class Solution:
    def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
        result, i = 0, -1

        if ruleKey == 'type':
            i = 0
        elif ruleKey == 'color':
            i = 1
        else:
            i = 2
        
        for j in range(len(items)):
            if items[j][i] == ruleValue:
                result += 1
        
        return result
