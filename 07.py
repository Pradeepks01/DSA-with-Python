# Reverse a number
class Solution:
    # Function to reverse digits of a number
    def reverseNumber(self, n):
        reve_num = 0
        while n > 0:
            lastdigit = n % 10
            reve_num =  reve_num * 10 + lastdigit
            n = n // 10
        return reve_num
x = Solution()
num = 12345
print(x.reverseNumber(num))