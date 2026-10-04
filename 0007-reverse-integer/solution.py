class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        reverse = 0
        while x:
            reverse = reverse * 10 + x % 10
            x //= 10

        reverse *= sign

        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0

        return reverse
