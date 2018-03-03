class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        z =str(x)
        lenx = len(z)
      
        if(x<0):
            y = "-"+z[lenx:0:-1]
            y =int(y)
            if(y<-2147483648):
                y = 0        
        else:
            y = z[::-1]
            y =int(y)
            if(y>2147483648):
                y=0
        return y
        
        
        
        
        
        
