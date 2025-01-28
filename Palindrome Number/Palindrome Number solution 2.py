import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x == 0:
            return True
        
        num_digits = math.floor(math.log10(x)) + 1
        
        print("num_digits: ", num_digits)
        i = 0

        while i < num_digits//2:

            rightDigit = (x % (10 ** (i+1))) // (10 ** i)
            leftDigit = (x // (10**(num_digits - i-1))) % 10
            print(rightDigit, leftDigit)
            if rightDigit != leftDigit:
                return False
            
            i = i+1

        return True
    
slt = Solution()

print(slt.isPalindrome(121))
