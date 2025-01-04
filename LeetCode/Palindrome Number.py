# Method - 1 (Two Pointers):
class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_x = str(x)
        left, right = 0, len(int_x) - 1
        while (left < right):
            if int_x[left] != int_x[right]:
                return False
            left += 1
            right -= 1
        return True

# Method - 2 (Using Remainder):
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x, x_copy = 0, x
        while (x > 0):
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return reversed_x == x_copy
  
