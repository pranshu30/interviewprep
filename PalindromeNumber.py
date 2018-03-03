class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        if(len(str(x))==1):
            return True
        if(x%10==0):
            return False
        else:
            revertnumber = 0
            while(x>revertnumber):
                revertnumber = revertnumber*10 +x%10
                x /=10
        return x==revertnumber or x == (revertnumber/10)
                    
        
