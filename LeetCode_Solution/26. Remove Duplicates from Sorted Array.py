def removeDuplicates(nums):
    left=1                                  #first pointer
    for right in range(1,len(nums)):        #second pointer
        if nums[right]!=nums[right-1]:      #checking for non-duplicates value
            nums[left]=nums[right]          #swapping the non-duplicate value to the left
            left+=1                         #increasing the left pointer as the left index has been filed with non-dupplicates values                       
    return left                             #returning the numbers of non-duplicate elemnet in nums after deleting the duplicate values

#Check
nums1=[1,1,2]                   #OUTPUT:2
nums2=[0,0,1,1,1,2,2,3,3,4]     #OUTPUT:5
print(removeDuplicates(nums1))
print(removeDuplicates(nums2))