import collections 

def containsDuplicate(nums):
    result= False
    for item in  collections.Counter(nums).values():         
        if item >1:
            result=True
    return result           
            
nums=[1,2,3,3]           
 
print(containsDuplicate(nums))

	# c=Counter(nums)
	# for i in c.items():
	# 	if i[1]!=1:
	# 		return True
	# return False