import collections, numpy
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for item in  collections.Counter(nums): 
            if item[1] !=1:
                return True
            else:
                return False
            
            
        
	# c=Counter(nums)
	# for i in c.items():
	# 	if i[1]!=1:
	# 		return True
	# return False