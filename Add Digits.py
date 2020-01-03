class Solution:
    def addDigits(self, num: int) -> int:
        #Recursive Method, if number is single digit (<10) return num, otherwise add digits and recur

        if num < 10:
            return num

        num = num % 10 + num // 10      #add digit to num and floor divide num to remove digit
        if num < 10:
            return num

        return self.addDigits(num)

    #Alt Solution: return num
    #if num == 0:
    #       return 0
    #    return num % 9 or 9
