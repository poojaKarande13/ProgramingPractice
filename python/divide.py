class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
            
        if divisor == 0:
            return None
        if dividend == 0:
            return 0
        if dividend > 0 and divisor > 0:
            return self.divideInternal(-divisor, -dividend)

        elif dividend > 0:
            return -self.divideInternal(divisor, -dividend)

        elif divisor > 0:
            return -self.divideInternal(-divisor,dividend)

        else:
            return self.divideInternal(divisor, dividend)

    def divideInternal(self,divisor, dividend):
        if dividend > divisor:
            return 0

        cur = 0
        res = 0

        while (divisor << cur) >= dividend and divisor<<cur < 0 :
            cur +=1

        res = dividend - (divisor << cur-1)
        if res > divisor:
            return 1 << cur-1
        return (1<<cur-1) + self.divide(res, divisor)