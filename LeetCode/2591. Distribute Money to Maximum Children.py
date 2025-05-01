class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money < 8:
            return 0
        if money > children * 8:
            return children - 1
        
        result = 0
        while money - 8 >= children - 1:
            money -= 8
            children -= 1
            result += 1
        
        if money == 4 and children == 1:
            result -= 1
        
        return result 
