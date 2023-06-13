def twoSum(nums,target):
	temp = []
	for i in range(0,len(nums)):
		for j  in range(i+1,len(nums)):
					if nums[i]+nums[j]==target:
						temp.append(i)
						temp.append(j)
	return temp			
						
print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
					