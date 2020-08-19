import math
class Solution:
    def isPowerOfFour(self,num):
        self.num=num
        if num > 0:
            return num == 1 or num == 4 or (math.log(num,4))-int(math.log(num,4))==0