class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        prod = 1
        su = 0
        while n:
            n, remainder = divmod(n, 10)
            digits.append(remainder)
        while digits:
            dig = digits.pop(len(digits) - 1)
            prod = prod * dig
            su = su + dig
        return prod - su