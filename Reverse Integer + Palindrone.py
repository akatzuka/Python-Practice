class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x > 0:
            rev = (10*rev) + x%10
            x //= 10
        return rev



    def palindrome(num):
            return str(num) == str(num)[::-1]
