class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        res = n

        while True:
            product = 1
            temp = res

            while temp > 0:
                digit = temp % 10
                product = product * digit
                temp = temp // 10

            if product % t == 0:
                return res

            res += 1