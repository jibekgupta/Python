'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2'''

def majorityElement(nums):
    res,count=0,0
    for n in nums:
        if count ==0:
            res=n
        count += (1 if n==res else -1)

    return res

#Check Case
nums1=[3,2,3]
nums2=[2,2,1,1,1,2,2]
print(majorityElement(nums1))           #OUTPUT: 3
print(majorityElement(nums2))           #OUTPUT: 2