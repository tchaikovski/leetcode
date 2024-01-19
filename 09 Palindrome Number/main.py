class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False

        temp = x
        reverse_num = 0
        while temp > 0:
            last_digit = temp % 10
            reverse_num = reverse_num * 10 + last_digit
            temp //= 10

        return x == reverse_num