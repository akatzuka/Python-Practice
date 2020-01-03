class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Power of 2 means only one bit of n is '1'
        #if -n AND n are equal to (n is greater than 0), then return true, otherwise return false
        #example 1: -1&1 (True) == 1>0 (True) ... True
        #example 2: -16&16 (True) == 16>0 (True) ... True
        #example 3: -218&218 (False) == 218>0 (True) ... False
        return-n&n==n>0     
