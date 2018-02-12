class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
       """
        final = []
        result = {}
        for i,j in enumerate(nums):
            secondnum = target - j
            if (secondnum in result.keys()):
                index = result[secondnum]
                if(i!=index):
                    final.append(i)
                    final.append(index)
                    break
            result[nums[i]]=i 
        return sorted(final) 
