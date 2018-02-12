class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        j=0
        n= len(s)
        dy =[]
        maxlen = 0           
        while(j<n):
            if(s[j] not in dy):
                dy.append(s[j])
                maxlen = max(maxlen,len(dy))
                j=j+1
            else:
                dy.pop(0)
                
        return maxlen
