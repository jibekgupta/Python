'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).'''

def removeDuplicates(nums):
    left=1                                  #first pointer
    for right in range(1,len(nums)):        #second pointer
        if nums[right]!=nums[right-1]:      #checking for non-duplicates value
            nums[left]=nums[right]          #swapping the non-duplicate value to the left
            left+=1                         #increasing the left pointer as the left index has been filed with non-dupplicates values                       
    return left                             #returning the numbers of non-duplicate elemnet in nums after deleting the duplicate values

#Check
nums1=[1,1,2]                   
nums2=[0,0,1,1,1,2,2,3,3,4]     
print(removeDuplicates(nums1))          #OUTPUT:2
print(removeDuplicates(nums2))          #OUTPUT:5